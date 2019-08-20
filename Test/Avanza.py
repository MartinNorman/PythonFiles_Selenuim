#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import time #To be able to sleep
#from datetime import datetime, timedelta
import codecs #To be able to write the file
#from selenium.webdriver.common.keys import Keys


#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Fund = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Link.set_page_load_timeout(30)
driver_Fund.set_page_load_timeout(30)

#########################################
## Start loop for each page where the funds are listed
#########################################

for page in range(1,45,1):
    print(page)
    #########################################
    ## Create empty file so we can write to it later
    #########################################
    Funds = codecs.open(r'C:\Users\clman\Documents\Funds\Funds_' + "%s" % page + '.txt', 'w', 'utf-8-sig')
    texttowrite = 'ID@Index@FundFee@PPM@Type@Category@ISIN@Morningstar@Risk@3Years@5Years@Responsible@Tag@Name'
    Funds.write(texttowrite + '\r\n')

    static = "https://www.avanza.se/fonder/lista.html?page="
    dynamic = str(page)
    sortorder = "&sortField=NAME&sortOrder=ASCENDING"
    driver_Link.get(static + dynamic + sortorder)
    Links = driver_Link.find_elements_by_xpath("//table[@id='contentTable']/child::tbody/descendant::tr/child::td[@class='overview tLeft fundListName']/child::a")

    #########################################
    ## For each page with fund links loop through each fund page
    #########################################
    for Link in Links:
        PreID = Link.get_attribute("href")
        CharToFind = '/'
        SlashIsAt = PreID.index(CharToFind, 44)
        ID = PreID[44:SlashIsAt]
        NameInLink = PreID[SlashIsAt+1:]
        print(ID)
        print(NameInLink)
        print(Link.get_attribute("href"))
        static = "https://www.avanza.se/fonder/om-fonden.html/"
        driver_Fund.get(static + ID + '/' + NameInLink)
        time.sleep(1)

        ####################################################
        ## Start extracting data
        ####################################################
#        time.sleep(1)
#        PreOneMonth = driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[1]/child::button/child::span[2]")
#        OneMonth = PreOneMonth.text
#        print(OneMonth)
#        PreThreeMonths = driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[2]/child::button/child::span[2]")
#        ThreeMonths = PreThreeMonths.text
#        print(ThreeMonths)
#        PreThisYear = driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[3]/child::button/child::span[2]")
#        ThisYear = PreThisYear.text
#        print(ThisYear)
#        PreOneYear = driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[4]/child::button/child::span[2]")
#        OneYear = PreOneYear.text
#        print(OneYear)
        PreThreeYears = driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[5]/child::button/child::span[2]")
        ThreeYears = PreThreeYears.text
        print(ThreeYears)
        PreFiveYears = driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[6]/child::button/child::span[2]")
        FiveYears = PreFiveYears.text
        print(FiveYears)
        PreRisk = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div[2]/aza-card[2]/aza-card-heading/div/h5")
        PreRisk2 = PreRisk.text
        Risk = PreRisk2.replace('\n', ',')
        print(Risk)
#        PreMorningstar = driver_Fund.find_elements_by_xpath("//ul[@class='rating ng-tns-c25-3 ng-star-inserted']/child::aza-icon[@name='morningstar-rating-yellow']")
        PreMorningstar = driver_Fund.find_elements_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div[2]/aza-card[3]/div/ul/aza-icon[@name='morningstar-rating-yellow']")
        Morningstar = int(len(PreMorningstar))
        print(Morningstar)
        PreTag = driver_Fund.find_element_by_xpath("//div[@class='tag-container']")
        PreTag2 = PreTag.text
        Tag = PreTag2.replace('\n', ',')
        print(Tag)
#        PreFundFee = driver_Fund.find_element_by_xpath("//h2[@class='ng-tns-c25-3']")
        PreFundFee = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div[2]/aza-card[1]/div/h3")
        FundFee = PreFundFee.text
        print(FundFee)
#        PreResponsible = driver_Fund.find_elements_by_xpath("//div[@class='fund-managers']//div[@class='ng-tns-c25-3 ng-star-inserted']")
        PreResponsible = driver_Fund.find_elements_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div/aza-card[2]/div/div[2]/div/div/div/div[@class='ng-tns-c26-3 ng-star-inserted']")
#        Responsible = PreResponsible.text
        #
        Responsible = ','.join(str(Person.text) for Person in PreResponsible)
        print("Responsible:")
        print(Responsible)

        ####################################################
        ## Switch tab to "Detaljer och nyckeltal"
        ####################################################
        driver_Fund.find_element_by_xpath("//aza-toggle-option[@value='details']").click()
        time.sleep(1)
    #    PreType = driver_Fund.find_element_by_xpath("//div[@class='column fund-details ng-tns-c25-3 ng-star-inserted']/child::div[1]/child::span[2]")
        PreType = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div/aza-card[2]/div/div[2]/div/div/div[1]/span[2]")
        Type = PreType.text
        print(Type)
#        PreCategory = driver_Fund.find_element_by_xpath("//div[@class='column fund-details ng-tns-c25-3 ng-star-inserted']/child::div[2]/child::span[2]")
        PreCategory = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div/aza-card[2]/div/div[2]/div/div/div[2]/span[2]")
        Category = PreCategory.text
        print(Category)
#        PreIndex = driver_Fund.find_element_by_xpath("//div[@class='column fund-details ng-tns-c25-3 ng-star-inserted']/child::div[4]/child::span[2]")
        PreIndex = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div/aza-card[2]/div/div[2]/div/div/div[4]/span[2]")
        Index = PreIndex.text
        print(Index)
#        PreISIN = driver_Fund.find_element_by_xpath("//div[@class='column fund-details ng-tns-c25-3 ng-star-inserted']/child::div[5]/child::span[2]")
        PreISIN = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div/aza-card[2]/div/div[2]/div/div/div[5]/span[2]")
        ISIN = PreISIN.text
        print(ISIN)

        ####################################################
        ## Switch tab to "Handelsinfo"
        ####################################################
        driver_Fund.find_element_by_xpath("//aza-toggle-option[@value='info']").click()
        time.sleep(1)
#        PrePPM = driver_Fund.find_element_by_xpath("//div[@class='tab-content columns ng-tns-c25-3 ng-trigger ng-trigger-fadeInAnimation ng-star-inserted']/child::div[3]/child::div[12]/child::label[2]")
        PrePPM = driver_Fund.find_element_by_xpath("/html/body/aza-app/main/aza-fund-guide/div/div[2]/div/aza-card[2]/div/div[2]/div/div/div[12]/label[2]")
        PPM = PrePPM.text
        print(PPM)
        ################################################
        ## Write to file
        ################################################
        #time.sleep(1)
        Funds.write("%s" %ID + "@" + "%s" %Index + "@" "%s" %FundFee + "@" + "%s" %PPM + "@" + "%s" %Type + "@" + "%s" %Category + "@" + "%s" %ISIN + "@" + "%s" %Morningstar + "@" + "%s" %Risk + "@" + "%s" %ThreeYears + "@" + "%s" %FiveYears + "@" + "%s" %Responsible + "@" + "%s" %Tag + "@" + "%s" %NameInLink + '\r\n')
        #time.sleep(1)


driver_Link.quit()
driver_Fund.quit()
