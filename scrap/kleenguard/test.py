from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('output2.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU input',
                     'SKU output', 'equal', 'url'])
count = 1
with open('input2.csv', newline='', encoding='utf-8-sig') as File:
    reader = csv.reader(File)
    for row in reader:
        url = row[2]
        sku = row[1]
        mfr = row[0]
        print(count)

        # url = 'https://www.na.kcprofessional.com/en-US/Products/Safety-and-Personal-Protection-Equipment/Disposable-Apparel/Liquid-Particulate-Protection/Liquid-and-Particle-Protection/KleenGuard-A40-Coveralls-White/27158'

        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        li = soup.find('li', class_='pdp__poduct-info__heading__product-code')
        code = li.text.split('#')
        prodCode = code[1]
        isEqual = False
        if(prodCode == sku):
            isEqual = True
        csv_writer.writerow([mfr, sku, prodCode, isEqual, url])
        count = count+1
csv_file.close()
