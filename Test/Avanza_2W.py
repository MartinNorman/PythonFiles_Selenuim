#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import time #To be able to sleep
from datetime import datetime, timedelta
import codecs #To be able to write the file
from selenium.webdriver.common.keys import Keys

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link_2W = webdriver.Chrome()
driver_Fund_2W = webdriver.Chrome()
driver_Link_2W.set_page_load_timeout(30)
driver_Fund_2W.set_page_load_timeout(30)

#########################################
## Start loop for each page where the funds are listed
## Improvement is to automatically figure out how many pages there are
#########################################

for page in range(1,45,1):
#    print(page)
    #########################################
    ## Create empty file so we can write to it later
    #########################################
    TwoWeek = codecs.open(r'C:\Users\clman\Documents\Funds\TwoWeek_' + "%s" %page + '.txt', 'w', 'utf-8-sig')
    texttowrite = 'ID@2W'
    TwoWeek.write(texttowrite + '\r\n')

    static = "https://www.avanza.se/fonder/lista.html?page="
    dynamic = str(page)
    driver_Link_2W.get(static + dynamic)
    Links = driver_Link_2W.find_elements_by_xpath("//table[@id='contentTable']/child::tbody/descendant::tr/child::td[@class='overview tLeft fundListName']/child::a")

    #########################################
    ## For each page with fund links loop through each fund page
    #########################################
    for Link in Links:
        PreID = Link.get_attribute("href")
        CharToFind = '/'
        SlashIsAt = PreID.index(CharToFind, 44)
        ID = PreID[44:SlashIsAt]
        NameInLink = PreID[SlashIsAt+1:]
#        print(ID)
#        print(NameInLink)
#        print(Link.get_attribute("href"))
        static = "https://www.avanza.se/fonder/om-fonden.html/"
        driver_Fund_2W.get(static + ID + '/' + NameInLink)


        ###############################################
        ##Get last 2 weeks result
        ###############################################

        To_Year = "2019"
        To_Month = "05"
        To_Day = "03"
        #To_Year = datetime.date(datetime.today() - timedelta(days=3)).year
        #Pre_To_Month = datetime.date(datetime.today() - timedelta(days=3)).month
        #To_Month = str(Pre_To_Month).zfill(2)
        #Pre_To_Day = datetime.date(datetime.today() - timedelta(days=3)).day
        #To_Day = str(Pre_To_Day).zfill(2)
        time.sleep(1)
        driver_Fund_2W.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()

        ###############################################
        ##Two weeks
        ###############################################
        From_Year = "2019"
        From_Month = "04"
        From_Day = "23"
        #vNo = 13
        #From_Year = datetime.date(datetime.today() - timedelta(days=vNo)).year
        #Pre_From_Month = datetime.date(datetime.today() - timedelta(days=vNo)).month
        #From_Month = str(Pre_From_Month).zfill(2)
        #Pre_From_Day = datetime.date(datetime.today() - timedelta(days=vNo)).day
        #From_Day = str(Pre_From_Day).zfill(2)

 #       print("Period to query", From_Year, From_Month, From_Day, " - ", To_Year, To_Month, To_Day, )
        ###################################################
        ## Set from date
        ##################################################
  #      time.sleep(1)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").click()
 #       time.sleep(1)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Month)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Day)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Year)
#        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
        driver_Fund_2W.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()
 #       PreValidateInputFrom = driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]")
#        ValidateInputFrom = PreValidateInputFrom.get_attribute('value')
 #       print(olle2)

        ###################################################
        ## Set to date
        ##################################################
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").click()
#        time.sleep(1)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Month)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Day)
        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Year)
#        driver_Fund_2W.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
        driver_Fund_2W.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()

  #      time.sleep(1)
        PreNoWeeks = driver_Fund_2W.find_element_by_xpath("//div[@class='chart-development']/child::span")
        NoWeeks = PreNoWeeks.text
#        print(NoWeeks)
        TwoWeek.write("%s" %ID + "@" + "%s" %NoWeeks + '\r\n')

driver_Link_2W.quit()
driver_Fund_2W.quit()
