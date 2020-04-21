from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('itw_scrapped.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU','Atrribute', 'Value', 'url'])

url = "https://www.itwprobrands.com/product/hdx"
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

title = soup.find('div', class_ = 'product-brand')
title = title.h1.text
print(title)

product_info = soup.find('div', class_ = 'information-product-holder')
product_info = soup.find('div', class_ = 'col-sm-6 col-xmd-12')
description = product_info.find('div', class_ = 'feature-holder').text.strip()
print(description)
# for features in product_info.find_all('div', class_ = 'feature-holder'):     features and apps
#     features = features.find('ul')
#     if features != None:
#         for features in features.find_all('li'):
#             if features != None:
#                 print(features.text.strip())

properties = soup.find('div', class_ = 'single-table')
table = properties.find('table')
table = properties.find_all('tbody')
print(table.tr)


