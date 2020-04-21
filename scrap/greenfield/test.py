
import csv

csv_file = open('links.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['SKU','Link'])
count = 1
with open('link_input.csv', encoding='utf-8-sig', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        sku = row[0]
        print(f'{count} : {sku}')
        link = f'https://www.gfii.com/pc_combined_results.asp?compsearch=0&search_prod=(searchlike~p.sku~{sku}|Or|searchlike~p.nm~{sku}|Or|searchlike~p.ds~{sku}|Or|searchlike~p.child_rollup_search_terms~{sku}|Or|searchlike~p.search_terms~{sku})&search_keyword={sku}'
        csv_writer.writerow([sku, link])
        print(sku)
csv_file.close()