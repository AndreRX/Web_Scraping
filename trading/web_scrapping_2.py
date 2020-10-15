import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

prices = []

options = Options()


url = "https://www.investing.com/currencies/us-dollar-index-advanced-chart"
driver = webdriver.Firefox(executable_path=r'C:\Users\Andre\Prog\geckodriver.exe', options=options)
driver.get(url)

def web_scraping():

    element = driver.find_element_by_xpath('//*[@id="last_last"]')
    html_content = element.get_attribute('innerHTML')

    
    driver.refresh()
    time.sleep(5)

    print(html_content)

    with open("cotations.txt", "a") as prices:
        prices.write(html_content + ",")

    return(web_scraping())


web_scraping()