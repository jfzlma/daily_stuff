from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('output.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU','Atrribute', 'Value', 'url'])
sku_list = ['02122',	'03910',	'03180',	'03120',	'1003364', '03095T',	'03189',	'14970',	'03151',	'03985',	'03995',	'03097',	'03183',	'03112',	'03116',	'03117',	'03118',	'03915',	'03113',	'14174',	'03184',	'14008',	'14418',	'14443',	'02023',	'03098',	'03188',	'03185',	'03121',	'14007',	'14407',	'14441',	'14408',	'14415',	'14416',	'03110',	'14170',	'14005',	'02018',	'03187',	'03916',	'1750016',	'03096',	'03111',	'10900',	'14171',	'14172',	'14440',	'02185',	'03100',	'03135',	'10321',	'03109',	'03114',	'02120',	'14406',	'14410',	'14414',	'14173']


for sku in sku_list :
    url = f'https://www.crcindustries.com/products/catalogsearch/result/?q={sku}'
    print(sku)

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    url = soup.find("meta",  property="og:url")['content']
    
    product_info = soup.find('div', class_ = 'product-shop')
    title = product_info.div.span.text
    csv_writer.writerow([sku, 'Title', title, url])                         #Writes title
    for description  in product_info.find_all('div', class_ = 'description') :
        description = description.text.split('\n')
        label = description[1].lstrip()
        value = description[2].lstrip()
        csv_writer.writerow([sku, label, value, url])                        # Writes Description
    try:
        item_no = product_info.find('div', class_ = 'skparts').span.text
        item_no = item_no.split(None)
        csv_writer.writerow([sku, item_no[0], item_no[1], url])                 #Writes No and Item No
        csv_writer.writerow([sku, item_no[3], item_no[4], url])
    except:
        pass

    for ul_list in soup.find_all('ul', class_ = 'data-attributes') :
        for odd_li in ul_list.find_all('li', class_ = 'odd-li') :
            label = odd_li.find('div', class_ = 'label').text
            data = odd_li.find('div', class_ = 'data').text
            #print(f"{label} : {data}")
            csv_writer.writerow([sku, label, data, url])

        for even_li in ul_list.find_all('li', class_ = 'even-li') :
            label = even_li.find('div', class_ = 'label').text
            data = even_li.find('div', class_ = 'data').text
                # print(f"{label} : {data}")
            csv_writer.writerow([sku, label, data, url])

csv_file.close()
