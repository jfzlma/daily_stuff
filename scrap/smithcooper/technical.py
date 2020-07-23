from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('technical.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['sku', 'Atrribute', 'Value', 'url'])
count = 1

with open('input.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:

        sku = row[0]
        url = row[1]

        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        print(count)

        try:

            table = soup.find('table', class_='table_page_content')
            td = table.find('td', id='middle_block')
            table2 = td.find('table')
            td2 = table2.find('td')
            for div in td2.find_all('div', class_='row'):
                div1 = div.find('div', class_='leftside')
                attribute = div1.text
                div2 = div.find('div', class_='visual_attraction')
                value = div2.text
                csv_writer.writerow([sku, attribute, value, url])
            count = count+1
        except:
            pass
            # print(attribute)
            # print(value)

        # td3 = table2.find('td', width='40%')
        # div3 = td3.find('div', class_='tech_info_block')
        # div4 = div3.find('div', class_='row clearfix first odd')
        # div5 = div4.find('div', class_='leftside')
        # attribute = div1.text
        # div6 = div4.find('div', class_='visual_attraction')
        # value = div2.text
        # print(attribute)
        # print(value)
csv_file.close()
