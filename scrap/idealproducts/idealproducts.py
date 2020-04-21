from bs4 import BeautifulSoup
import requests
import csv
# csv_file = open('idealproducts.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['SKU','link'])
#sku_list = ['02122',	'03910',	'03180',	'03120',	'1003364', '03095T',	'03189',	'14970',	'03151',	'03985',	'03995',	'03097',	'03183',	'03112',	'03116',	'03117',	'03118',	'03915',	'03113',	'14174',	'03184',	'14008',	'14418',	'14443',	'02023',	'03098',	'03188',	'03185',	'03121',	'14007',	'14407',	'14441',	'14408',	'14415',	'14416',	'03110',	'14170',	'14005',	'02018',	'03187',	'03916',	'1750016',	'03096',	'03111',	'10900',	'14171',	'14172',	'14440',	'02185',	'03100',	'03135',	'10321',	'03109',	'03114',	'02120',	'14406',	'14410',	'14414',	'14173']
sku_list = ['70-1117',	'70-4200',	'70-1160',	'70-1104',	'70-1000',	'70-1170',	'70-1180q',	'70-1150',	'70-1100',	'70-1110',	'70-1090',	'70-1080',	'70-1020',	'70-1030',	'70-1061',	'70-1062',	'70-1063',	'70-1064',	'70-1065',	'70-1065-1',	'70-1065-2',	'70-1065-3',	'70-1070',	'70-1071',	'70-1072',	'70-1073',	'70-1074',	'70-1075',	'70-1076',	'70-1077',	'70-1078',	'70-1079',	'70-1091-1',	'70-1095-1',	'70-1187',	'70-1186']


for sku in sku_list :
    url = f'https://distributors.idealwarehouse.com/?s={str(sku)}&post_type=product'
    print(sku)


    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    url = soup.find("meta",  property="og:url")['content']
    print(url)
    # csv_writer.writerow([sku, url])
    try:
        title = soup.find('div', class_ = 'entry-summary')
        title = title.find('div', class_ = 'et_pb_section et_pb_section_1 product-page et_pb_with_background et_section_regular')
        title = title.find('div', class_= 'et_pb_row et_pb_row_0')
        title = title.find('div', class_ = 'clearfix et_pb_module et_pb_woo_title et_pb_bg_layout_light et_pb_text_align_ et_pb_woo_title_0 ')
        print(title.h1.text)
    except:
        pass   
#     product_info = soup.find('div', class_ = 'product-shop')
#     title = product_info.div.span.text
#     csv_writer.writerow([sku, 'Title', title, url])                         #Writes title
#     for description  in product_info.find_all('div', class_ = 'description') :
#         description = description.text.split('\n')
#         label = description[1].lstrip()
#         value = description[2].lstrip()
#         csv_writer.writerow([sku, label, value, url])                        # Writes Description
#     try:
#         item_no = product_info.find('div', class_ = 'skparts').span.text
#         item_no = item_no.split(None)
#         csv_writer.writerow([sku, item_no[0], item_no[1], url])                 #Writes No and Item No
#         csv_writer.writerow([sku, item_no[3], item_no[4], url])
#     except:
#         pass

#     for ul_list in soup.find_all('ul', class_ = 'data-attributes') :
#         for odd_li in ul_list.find_all('li', class_ = 'odd-li') :
#             label = odd_li.find('div', class_ = 'label').text
#             data = odd_li.find('div', class_ = 'data').text
#             #print(f"{label} : {data}")
#             csv_writer.writerow([sku, label, data, url])

#         for even_li in ul_list.find_all('li', class_ = 'even-li') :
#             label = even_li.find('div', class_ = 'label').text
#             data = even_li.find('div', class_ = 'data').text
#                 # print(f"{label} : {data}")
#             csv_writer.writerow([sku, label, data, url])

# csv_file.close()
