import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

prices = []

options = Options()
options.set_headless()


def web_scraping():
    url = "https://www.investing.com/currencies/us-dollar-index-advanced-chart"

    driver = webdriver.Firefox(executable_path=r'C:\Users\Andre\Prog\geckodriver.exe', options=options)
    driver.get(url)

    element = driver.find_element_by_xpath('//*[@id="last_last"]')
    html_content = element.get_attribute('innerHTML')

    driver.quit()
    
    print(html_content)

    with open("test.csv", "a") as prices:
        writer = csv.writer(prices)
        writer.writerow(html_content)


    return(web_scraping())


web_scraping()