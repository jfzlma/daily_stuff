from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('tapes', 'w', encoding='utf-8-sig', newline='')
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
            brand = soup.find('a', class_='brand solr-brand').text
            csv_writer.writerow([sku, 'Brand', brand])
            title = soup.find('h1', class_='productName').text.strip()
            csv_writer.writerow([sku, 'Title', title])
            details = soup.find('div', id='additionalInfoSection')
            deta = details.find('div', id='copyTextSection')
            descr = deta.text.strip()
            csv_writer.writerow([sku, 'Product Details', descr])

        except:
            pass
        try:
            col = soup.find('ul', class_='column')
            for li in col.find_all('li'):
                attribute = li.find('span', class_='specName').text
                value = li.find('span', class_='specValue').text
                csv_writer.writerow([sku, attribute, value])
            count += 1
        except:
            csv_writer.writerow([sku, 'null', 'null'])
            count += 1
csv_file.close()
