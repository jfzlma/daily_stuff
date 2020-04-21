from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('velocity_boiler.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([' ','link'])



url = 'https://www.velocityboilerworks.com/product/aruba-4-awr/'
with open('page.html') as source:
    soup = BeautifulSoup(source, 'lxml')

#source = requests.get(url).text
article = soup.find('article')
print(f'Title: {article.header.h1.text}')
title = article.header.h1.text

descr = soup.find('div', 'col-sm-8 col-sm-pull-4')
for p in descr.find_all('p'):
    print(p.text)
    csv_writer.writerow([title, 'Description', p.text, url])


tab_content = soup.find('div', class_ = 'tab-content')
table = tab_content.find('table')
for tr in table.find_all('tr'):
    values = [title]
    for td in tr.find_all('td') :
        values.append(td.text)
    print(values)
    values.append(url)
    csv_writer.writerow(values)
# print(tab_content.prettify())
try:
    second_table = soup.find('div', class_ = 'scroll-note')
    # table = second_table.find('table')
    # table = table.find('tbody')
    for data in second_table.find_all('tr', class_ = 'row1c') :
        values = []
        for td in data.find_all('td') :
            values.append(td.text)
        print(values)
except:
    pass


# print(tabs)
# csv_writer.writerow([sku, url])
# csv_file.close()
