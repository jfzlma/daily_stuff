from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('output2.csv', 'w', newline = '')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU ip', 'link','sku op', 'attribute', 'value'])
count, fail, succ = 1, 0, 0
with open('input.csv', newline='') as input:
    reader = csv.reader(input)
    for row in reader:
        try:
            sku = row[0]
            print(f'count: {count}, sku: {sku}')
            url = f'https://www.natool.com/?s={sku}&post_type=product'
            source = requests.get(url)
            act_url = source.url
            source = source.text
            soup = BeautifulSoup(source, 'lxml')

            main = soup.find('div', class_='ts-col-18')
            primary = main.find('div', class_ =  'site-content')
            product = primary.find('div', class_= 'vertical-thumbnail')
            summary = product.find('div', class_= 'summary')
            sku_op = summary.find('div', class_='sku-wrapper')
            sku_op = sku_op.span.text

            # print(sku_op)
            # title_div = summary.find('div', class_= 'single-navigation')
            title = summary.h1.text
            # print(title)
            #csv_writer.writerow([str(sku), act_url, sku_op, 'Title', title])
            print([str(sku), act_url, sku_op, 'Title', title])

            table_div = product.find('div', class_= 'wccpf-admin-fields-group-1')
            # print(table.prettify())
            for table in table_div.find_all('table'):
                values = [str(sku), act_url, sku_op]
                td_attribute = table.find('td', class_ = 'wccpf_label')
                attribute = td_attribute.label.text
                value = table.find('td', class_ = 'wccpf_value').input['value']
                values.append(attribute)
                values.append(value)
                csv_writer.writerow(values)
            count += 1
            succ = succ+1
        except:
            print(f'{count} pass')
            count += 1
            fail = fail+1

csv_file.close()
print(f'Failed: {fail}, success: {succ}')


