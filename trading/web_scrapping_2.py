import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

prices = []

options = Options()


url = "https://www.investing.com/currencies/us-dollar-index-advanced-chart"
driver = webdriver.Firefox(executable_path=r'C:\Users\andre\Desktop\Web_Scraping\geckodriver.exe', options=options)
driver.get(url)

file_path = "C:\\Users\\andre\\Desktop\\Web_Scraping\\trading\\cotations.txt"

def web_scraping():

    element = driver.find_element_by_xpath('//*[@id="last_last"]')
    html_content = element.get_attribute('innerHTML')

    
    driver.refresh()
    

    print(html_content)

    with open(file_path, "a") as prices:
        prices.write(html_content + ",")

    time.sleep(5)
    return(web_scraping())


web_scraping()