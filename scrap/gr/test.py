from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('tapes-unit2.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU', 'Atrribute', 'Value', 'url'])
count = 1

with open('input.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:

        sku = row[0]
        url = f'https://www.grainger.com/product/{sku}'
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }
        try:
            source = requests.get(url, headers=headers).text
            soup = BeautifulSoup(source, 'lxml')
        except:
            print('connection error')

        print(count)
        try:
            span = soup.find('span', class_='gcprice-value')
            unit = span.find('span', class_='gcprice-unit').text.strip('/ ')
            print(unit)
            csv_writer.writerow([sku, unit])
        except:
            csv_writer.writerow([sku, 'null', 'null'])
            count += 1
        try:
            unit2 = span.find(
                'p', class_='gcprice gcprice-shipPack gcprice-idp').text.strip()
            print(unit2)
            csv_writer.writerow([sku, unit2])
        except:
            csv_writer.writerow([sku, 'null', 'null'])
            count += 1


csv_file.close()
