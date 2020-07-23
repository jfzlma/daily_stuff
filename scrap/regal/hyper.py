from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('hyperlink.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['mfr', 'sku', 'attribute', 'url'])
count = 1

with open('hyper_input.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:
        mfr = row[0]
        sku = row[1]
        url = row[2]

        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }
        # url = 'https://www.regalbeloit.com/products/motors/low-voltage-nema-motors/hvac-r-motors/fan-and-blower-motors/belt-drive-motors/1-6-hp-fan-and-blower-hvac-r-motor-1-phase-1200-rpm-115-v-56z-frame-teao-arb2016m?showSpin=true'
        print(count)
        try:
            source = requests.get(url, headers=headers).text
            soup = BeautifulSoup(source, 'lxml')

            div = soup.find_all('div', class_='container-fluid')[11]
            row = div.find('div', class_='row')
            section = div.find_all('div', class_='section')[1]

            for col in section.find_all('div', class_='col-lg-3 col-md-4 col-sm-6'):
                title = col.find('div', class_='magic-button__title').text
                link = col.a['href']
                csv_writer.writerow([mfr, sku, title, link])
            count += 1
        except:
            count += 1
            print('pass')
