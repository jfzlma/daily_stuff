from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('missing_scrapped.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['sku', 'mfr', 'attribute', 'value', 'url'])
count = 1

with open('missing.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:
        sku = row[0]
        mfr = row[1]
        url = row[2]
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }
        print(count)
        source = requests.get(url, headers=headers).text
        soup = BeautifulSoup(source, 'lxml')
        try:
            title_div = soup.find('div', class_='page-title')
            title = title_div.h1.text.strip()
            csv_writer.writerow([sku, mfr, 'Title', title, url])

            feature_div = soup.find('div', class_='product-info text-guide')
            ul = feature_div.find('ul')
            features = ''
            for li in ul.find_all('li'):
                features = features + li.text.strip() + '; '
            csv_writer.writerow([sku, mfr, 'Features', features, url])

            panel_body = soup.find('div', class_='panel-body text-guide')

            for table in panel_body.find_all('table'):
                for tr in table.find_all('tr'):
                    attribute = tr.find_all(
                        'td', class_='specifications-table_col col-md-2 pull-left')
                    value = tr.find_all(
                        'td', class_='specifications-table_col col-md-4 pull-left')

                    index = 0
                    for attr in attribute:
                        attrb = attribute[index].text
                        val = value[index].text
                        index += 1
                        csv_writer.writerow([sku, mfr, attrb, val, url])
            count = count+1
        except:
            print('pass')
            csv_writer.writerow([sku, mfr, 'pass', 'pass', 'pass'])
            count = count+1
