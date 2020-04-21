import csv
from selenium import webdriver
from PIL import Image

#Opens url in chrome and take screenshot


with open('ss.csv', 'r', encoding='utf-8-sig') as file:
    driver = webdriver.Chrome()
    reader = csv.reader(file)
    for row in reader:
        
        driver.get(row[1])
        # element = driver.find_element_by_id("hplogo")
        # location = element.location
        # size = element.size
        driver.save_screenshot(f'{row[0]}.jpg')
        print(f'{row[1]} --> {row[0]}')
    