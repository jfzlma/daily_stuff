from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('dimension.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['sku', 'Atrribute', 'Value', 'url'])
count = 1

with open('input.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:

        sku = row[0]
        url = row[1]
        print(count)
        try:

            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')

            div = soup.find('div', id='outer_wrapper')
            div2 = div.find('div', id='inner_wrapper')
            div3 = div2.find('div', id='middle_container')
            div4 = div3.find('div', id='all_content')
            table = div4.find('table', class_='table_page_content')
            td = table.find('td', id='middle_block')
            div5 = td.find('div', id='page_content')
            table2 = div5.find('table')
            tr = table2.find('tr')
            td2 = tr.find('td', width='40%')
            div5 = td2.find('div', class_='tech_info_block')

            div6 = div5.find('div', class_='row clearfix first odd')
            attribute = div6.find('div', class_='leftside').text
            value = div6.find(
                'div', class_='visual_attraction rightside A').text

            csv_writer.writerow([sku, attribute, value, url])

            div6 = div5.find('div', class_='row clearfix last even')
            attribute = div6.find('div', class_='leftside').text
            value = div6.find(
                'div', class_='visual_attraction rightside B').text

            csv_writer.writerow([sku, attribute, value, url])
            count = count+1
        except:
            print(f'pass {sku}')

csv_file.close()
