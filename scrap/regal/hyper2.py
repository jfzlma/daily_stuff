from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('outline_out.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['mfr', 'sku', 'attribute', 'url'])
count = 1

with open('outline.csv', newline='', ) as File:
    reader = csv.reader(File)
    for row in reader:
        mfr = row[0]
        sku = row[1]
        url = row[3]

        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }
        # url = 'https://www.regalbeloit.com/products/motors/low-voltage-nema-motors/hvac-r-motors/fan-and-blower-motors/belt-drive-motors/1-6-hp-fan-and-blower-hvac-r-motor-1-phase-1200-rpm-115-v-56z-frame-teao-arb2016m?showSpin=true'
        print(count)

        source = requests.get(url, headers=headers)
        link = source.url
        csv_writer.writerow([mfr, sku, link])
