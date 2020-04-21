from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('osg_scrapped.xlsx', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU','link'])
count = 1
with open('input.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        try:
            print(count)
            url = row[1]
            sku = row[0]
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            
