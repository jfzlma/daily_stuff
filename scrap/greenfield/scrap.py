from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('output4.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU','Attribute', 'Value', 'Link'])
count = 1
success, failed = 0, 0
fail_sku = []

with open('input_3.csv', encoding='utf-8-sig', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        try:
            
            sku = row[0]
            print(f'{count} : {sku}')
            link = f'https://www.gfii.com/pc_combined_results.asp?compsearch=0&search_prod=(searchlike~p.sku~{sku}|Or|searchlike~p.nm~{sku}|Or|searchlike~p.ds~{sku}|Or|searchlike~p.child_rollup_search_terms~{sku}|Or|searchlike~p.search_terms~{sku})&search_keyword={sku}'
            source = requests.get(link)
            act_url = source.url
            source = source.text
            soup = BeautifulSoup(source, 'lxml')
            print(act_url)

            data = soup.find('div', class_ = 'content_padding full')
            data1 = soup.find('div', class_ = 'content fixed')
            data2 = soup.find('div', id = 'detail_wrap')
            data3 = soup.find('div', class_ = 'detail_cart')
            data4 = soup.find('div', class_ = 'gfi')
            
            for ul in data4.find_all('ul') :
                
                for li in ul.find_all('li') :
                    atrribute = li.span.text
                    value = li.text.split()[-1]
                    csv_writer.writerow([str(sku), atrribute, value, act_url])
            count+=1
            success+=1
        except:
            csv_writer.writerow([str(sku), 'err'])
            print(f'{count} pass')
            count+=1
            failed+=1
            fail_sku.append(sku)
print(f'Success : {success}')
print(f"Failed : {failed-2}")

csv_writer.writerow(fail_sku)
csv_file.close()