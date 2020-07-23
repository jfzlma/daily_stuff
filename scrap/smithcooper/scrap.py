from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('output3.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Atrribute', 'Value', 'url'])
count = 1
sku_range = range(69400, 70000)
urls = ['https://www.smithcooper.com/catalogue/product/74752', 'https://www.smithcooper.com/catalogue/product/75840', 'https://www.smithcooper.com/catalogue/product/74756', 'https://www.smithcooper.com/catalogue/product/74760', 'https://www.smithcooper.com/catalogue/product/74765', 'https://www.smithcooper.com/catalogue/product/75844', 'https://www.smithcooper.com/catalogue/product/74766',
        'https://www.smithcooper.com/catalogue/product/75845', 'https://www.smithcooper.com/catalogue/product/74767', 'https://www.smithcooper.com/catalogue/product/75846', 'https://www.smithcooper.com/catalogue/product/74768', 'https://www.smithcooper.com/catalogue/product/75847', 'https://www.smithcooper.com/catalogue/product/74770', 'https://www.smithcooper.com/catalogue/product/74771', 'https://www.smithcooper.com/catalogue/product/74772']

for url in urls:
    try:
        # url = f'https://www.smithcooper.com/catalogue/product/{sku}'
        print(f'{count}: ')
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('table', class_='table_page_content')
        td = table.find('td', id='middle_block')
        table2 = td.find('table', class_='comp_reg_view')
        div = table2.find('div', class_='techdet')

        for row in div.find_all('div', class_='row'):
            attr = row.find('div', class_='field_name leftside').text
            value = row.find('div', class_='field_data rightside').text
            csv_writer.writerow([attr, value, url])
        count = count+1
    except:
        pass
csv_file.close()
