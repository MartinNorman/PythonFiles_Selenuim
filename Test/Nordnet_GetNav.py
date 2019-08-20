#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import time #To be able to sleep
from datetime import datetime
import codecs #To be able to write the file

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Fund = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Fund.set_page_load_timeout(30)

#########################################
##Static paths and variables
#########################################
static1 = "https://secust.msse.se/se/nordnetny/funds/overview.aspx?cid="
static2 = "&cntry=SE" #&amp;IPS=1&amp;istopp3=0&amp;expert=&amp;nnkat=&amp;site=se&amp;lang=sv&amp;orderaction=onlybuy
vDate = datetime.now().strftime("%Y-%m-%d")


#########################################
## Create empty file so we can write to it later
#########################################
Nordnet_Nav = codecs.open(r'W:\Martin\Nordnet\Result\Nav' + vDate + '.txt', 'w', 'utf-8')


#########################################
## Get IDs to read
#########################################
with codecs.open('C:/Users/clman/Documents/Funds/Nordnet/ID.txt', 'r', encoding='utf-8') as Funds:
    for Fund in Funds:
        Fund2 = Fund.strip()
#        print(static)
        driver_Fund.get(static1 + Fund2 + static2)
#        time.sleep(1)
        print(static1 + Fund2 + static2)
        print(vDate)
        Nav = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[4]")
        Nav = Nav.text
        print(Nav)

################################################
## Write to file
################################################
        Nordnet_Nav.write("%s" %Fund2 + "@" + "%s" %Nav + "@" "%s" %vDate + '\r\n')

driver_Fund.quit()
