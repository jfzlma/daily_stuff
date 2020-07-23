# coding=utf-8
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
count = 1
with open('test.xlsx', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    driver = webdriver.Chrome()
    reader = csv.reader(file)
    for row in reader:
        try:

            driver.get('https://www.se.com/in/en/product/ATV320U04M2B')
            time.sleep(10)
        except:
            pass
