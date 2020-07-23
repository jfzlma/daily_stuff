from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('schn2.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU', 'Atrribute', 'Value', 'url'])
count = 1

with open('input.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:

        sku = row[0]
        url = f'https://www.se.com/ww/en/product/{sku}'
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }
        source = requests.get(url, headers=headers).text
        soup = BeautifulSoup(source, 'lxml')

        print(count)
        try:
            title = soup.find(
                'h2', class_='pdp-product-info__description').text.strip()
            drawer = soup.find('div', class_='drawer')
            ul = drawer.find('ul', class_='characteristics-list')
            li = ul.find('li', class_='characteristics-list__item')
            for table in li.find_all('table', class_='pes-table'):
                for tr in table.find_all('tr'):
                    attribute = tr.th.text.strip()
                    value = tr.td.div.text.strip()
                    # print(attribute, value)
                    csv_writer.writerow([sku, attribute, value, url])
            count = count+1
        except:
            csv_writer.writerow([sku, 'pass', 'pass', url])
            print('pass')
            count = count+1
csv_file.close()
