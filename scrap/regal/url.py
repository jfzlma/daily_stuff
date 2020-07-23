from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('links2.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU', 'url', 'part'])
count = 1

with open('input.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:
        sku = row[0]
        url = f'https://www.regalbeloit.com/search/products?query={sku}'
        # headers = {
        #     'User-Agent': 'My User Agent 1.0',
        #     'From': 'youremail@domain.com'  # This is another valid field
        # }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        source = requests.get(url, headers=headers).text
        soup = BeautifulSoup(source, 'lxml')
        print(count)
        try:
            table = soup.find('table', class_='category-view-list')
            div = table.find(
                'div', class_='td-product-info__img td-product-info__img-lg')

            link = f"https://www.regalbeloit.com/{div.a['href']}"
            # print(url)

            div2 = table.find('div', class_='td-product-info__info')
            # print(div2.prettify())

            param = div2.find('div', class_='td-product-param')
            partNum = param.find('span', class_='param-row__value').text

            csv_writer.writerow([sku, link, partNum])
            count = count+1
        except:
            csv_writer.writerow([sku, 'pass', 'pass'])
            print('pass')
            count = count+1
