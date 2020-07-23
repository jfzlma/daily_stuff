from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('output.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU',
                     'Atrribute', 'Value', 'url'])
count = 1
with open('input.csv', newline='', encoding='utf-8-sig') as File:
    reader = csv.reader(File)
    for row in reader:
        url = row[1]
        sku = row[0]
        print(count)
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        div1 = soup.find('div', class_='col-12 col-md-7 col-lg-7')
        para = div1.p.text
        csv_writer.writerow([sku, url, 'Description', para])
        ul = div1.ul
        features = ''
        for li in ul.find_all('li'):
            features = features + li.text.strip() + '; '

        csv_writer.writerow([sku, url, 'features', features])

        div2 = soup.find(
            'div', class_='accordions__item__content sec__hide__specifications_content')
        # print(div2)

        for row in div2.find_all('div', class_='row'):
            table = row.find('table')
            for tr in table.find_all('tr'):
                values = [sku, url]
                for td in tr.find_all('td'):
                    # print(td.text)
                    values.append(td.text)
                csv_writer.writerow(values)
        count = count+1
csv_file.close()
