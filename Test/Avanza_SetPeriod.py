from selenium import webdriver
import time
from datetime import datetime, timedelta
import codecs #To be able to write the file
from selenium.webdriver.common.keys import Keys


#########################################
## Create empty file so we can write to it later
#########################################
tmp = codecs.open(r'C:\Users\clman\Documents\Funds\OneWeek.txt', 'w', 'utf-8-sig')
texttowrite = 'ID@OneWeek'
tmp.write(texttowrite + '\r\n')


driver_Fund = webdriver.Chrome()
driver_Fund.set_page_load_timeout(15)

static = "https://www.avanza.se/fonder/om-fonden.html/"
ID = "951763"
NameInLink = "jpm-us-technology-a-acc-usd"
driver_Fund.get(static + ID + '/' + NameInLink)

To_Year = datetime.date(datetime.today() - timedelta(days=1)).year
Pre_To_Month = datetime.date(datetime.today() - timedelta(days=1)).month
To_Month = str(Pre_To_Month).zfill(2)
Pre_To_Day = datetime.date(datetime.today() - timedelta(days=1)).day
To_Day = str(Pre_To_Day).zfill(2)
#print(To_Year)
#print(To_Month)
#print(To_Day)

driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()

for No in range(1,4):
    vNo = No * 2
    From_Year = datetime.date(datetime.today() - timedelta(days=vNo)).year
    Pre_From_Month = datetime.date(datetime.today() - timedelta(days=vNo)).month
    From_Month = str(Pre_From_Month).zfill(2)
    Pre_From_Day = datetime.date(datetime.today() - timedelta(days=vNo)).day
    From_Day = str(Pre_From_Day).zfill(2)
    print(From_Year)
    print(From_Month)
    print(From_Day)

    ###################################################
    ## Set from date
    ##################################################

    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").click()
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Year)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Day)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Month)
    driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()
    ###################################################
    ## Set to date
    ##################################################
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").click()
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Year)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Day)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
    driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Month)
    driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()
    PreNoWeeks = driver_Fund.find_element_by_xpath("//div[@class='chart-development']/child::span")
    NoWeeks = PreNoWeeks.text
    print(NoWeeks)
# ##################################################
# ## Set from date One Week
# ##################################################
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").click()
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Year_OneWeek)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Day_OneWeek)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(Keys.ARROW_LEFT)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[1]").send_keys(From_Month_OneWeek)
# driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()
# ##################################################
# ## Set to date One Week
# ##################################################
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").click()
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Year)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Day)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(Keys.ARROW_LEFT)
# driver_Fund.find_element_by_xpath("//div[@class='date-pickers ng-star-inserted']/child::input[2]").send_keys(To_Month)
# driver_Fund.find_element_by_xpath("//div[@class='periods-wrapper']/child::aza-period-button[8]").click()
# PreOneWeek = driver_Fund.find_element_by_xpath("//div[@class='chart-development']/child::span")
# OneWeek = PreOneWeek.text
# print(OneWeek)


time.sleep(1)

time.sleep(2)
