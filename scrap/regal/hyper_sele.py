import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time

csv_file = open('outline_selen.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU', 'mfr', 'link'])
count = 1

with open('outline.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    driver = webdriver.Chrome()
    reader = csv.reader(file)
    for row in reader:

        lin = row[2]

        driver.get(lin)
        time.sleep(5)
        link = driver.current_url

        csv_writer.writerow([row[0], row[1], link])
        print(count)
        count = count+1
