import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

csv_file = open('muthai/output.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU', 'mfr', 'link'])
count = 1

with open('muthai/input.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    driver = webdriver.Chrome()
    reader = csv.reader(file)
    for row in reader:
        driver.get('https://www.regalbeloit.com/')
        try:
            input = driver.find_element_by_xpath(
                "//input[@id='txtSearchGlobal']")
            mfr = row[1]
            sku = row[0]
            input.send_keys(mfr)
            button = driver.find_element_by_xpath(
                "//button[@id='btnSearch']")
            button.click()
            link = driver.current_url
            csv_writer.writerow([sku, mfr, link])
        except:
            pass
