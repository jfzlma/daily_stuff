from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('osg_scrapped.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU','Atrribute', 'Value', 'url'])
count = 1
with open('input.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        try:
            print(count)
            url = row[1]
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')

            body = soup.find('section', id='drilling')
            title = body.h4.text.strip()
            # print(title)

            table = body.find('div', class_ = 'table-responsive')
            material_num = table.h3.text
            attribute = material_num.split(':')[0]
            value = material_num.split()[2]
            sku = value
            # print(attribute)
            # print(value)

            csv_writer.writerow([sku, 'Title', title])
            csv_writer.writerow([sku, attribute, value])
            print(f'{count}: got title')


            table = table.find('table', class_ = 'table table-striped')
            tbody = table.find('tbody')

            for tr in tbody.find_all('tr') :
                attr = [sku]
                for td in tr.find_all('td') :
                    attr.append(td.text)
                csv_writer.writerow(attr)
            print(f'{count}: got table data')
            count+=1
        except:
            print(f'{count} pass')
            count+=1

csv_file.close()
        
