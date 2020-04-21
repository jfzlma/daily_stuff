import csv
ulr_list = []
with open('input.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        ulr_list.append(row[0])
        print(row[1])

# print(ulr_list)