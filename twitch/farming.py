import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()


url = "link"
driver = webdriver.Firefox(executable_path=r'C:\Users\andre\Desktop\Web_Scraping\geckodriver.exe', options=options)
driver.get(url)

test = '/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button/span/div/div/div/svg/g/path'


def web_scraping():
    
    try :
        element = driver.find_element_by_xpath(test)
        element.click()
        
        print("sucesso")
        time.sleep(30)
        return(web_scraping())
    
    except:
        print("erro")
        time.sleep(30)
        return(web_scraping())




web_scraping()