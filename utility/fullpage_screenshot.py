#coding=utf-8                                                                                                                                                                              
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
count = 1
with open('input.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    reader = csv.reader(file)
    for row in reader:

        # URL = 'https://pythonbasics.org/selenium-screenshot/'

        driver.get(row[1])

        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
        driver.find_element_by_tag_name('body').screenshot(f'screenshot/{row[0]}.jpg')
        print(count)
        count+=1


driver.quit()