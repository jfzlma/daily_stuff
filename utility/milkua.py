# coding=utf-8
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
count = 1
with open('input_milk.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    reader = csv.reader(file)
    for row in reader:
        try:

            driver.get(row[1])
            time.sleep(10)

            try:
                read_more = driver.find_element_by_xpath(
                    "//*[@data-readmore-toggle='rmjs-1']")
                read_more.click()
            except:
                pass

            try:

                read_more2 = driver.find_element_by_xpath(
                    "//*[@data-readmore-toggle='rmjs-2']")
                read_more2.click()
            except:
                pass

            def S(X): return driver.execute_script(
                'return document.body.parentNode.scroll'+X)
            # driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
            driver.set_window_size(1200, 3500)  # May need manual adjustment
            driver.find_element_by_tag_name(
                'body').screenshot(f'milk/{row[0]}.jpg')
            print(count)
            count += 1
        except:
            print('pass')


driver.quit()
