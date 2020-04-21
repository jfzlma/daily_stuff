from bs4 import BeautifulSoup
import requests
import csv

# csv_file = open('osg_scrapped.xlsx', 'w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['SKU','link'])
# count = 1

# csv_file = open('osg_scrapped.xlsx', 'w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['SKU','link'])
# count = 1
url = 'https://www.walter-tools.com/en-us/search/pages/default.aspx#/product/A1247-3~2F16IN'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

link = soup.find('div', id= 's4-bodyContainer')
link = link.find('div', class_= 'content')
# link = link.find('div', class_= 'ng-scope')
# link = link.find('div', class_= 'col-sm-12')

# # ng_if_Att =  [values['ng-if'] for values in soup.findAll("a")]
# href_link =  [values['href'] for values in soup.findAll("a")]

# # print('ng_if attr = {0}'.format(ng_if_Att[0]))
# print('href_link attr = {0}'.format(href_link[0]))  

for link in link.find_all('a') :
    print(link.prettify())
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')