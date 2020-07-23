from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('3m_output.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Material','Mfr No', 'Atrribute', 'Value'])
count = 1

with open('input.csv', newline='', encoding='utf-8-sig') as File:
    reader = csv.reader(File)
    for row in reader:
        print(count)

        material = row[0]
        mfr = row[1]
        url = row[2]
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        head = soup.find('h1', class_= 'MMM--hdg MMM--hdg_1 hdg_contentDetailTitle').text
        # print(head.strip())
        csv_writer.writerow([material, mfr, 'Heading', head.strip()])
        specs = soup.find('div', class_= 'productSpecs')
        table = specs.find('table', class_= 'MMM--dat MMM--pdpTabVr SNAPS--SpecTbl-Mt15')
        for tr in table.find_all('tr', class_='MMM--dat-row'):
            values = [material, mfr]
            for td in tr.find_all('td'):
                # attribute = td.span.text
                values.append(td.span.text)
            # print(values)
            csv_writer.writerow(values)
        count+=1
csv_file.close()
