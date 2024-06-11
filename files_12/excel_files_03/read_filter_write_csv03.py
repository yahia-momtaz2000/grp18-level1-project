# program to read from excel and filter data based on Cairo and write to another excel file
import csv

with open('C:\\MY_FILES\\people.csv', 'r') as f1, open('C:\\MY_FILES\\people_filtered.csv', 'w', newline='') as f2:
    reader_list = csv.reader(f1)
    writer_pen = csv.writer(f2)
    writer_pen.writerow(['Name', 'Age', 'City'])
    for row in reader_list:
        if row[2] == 'Cairo':
            writer_pen.writerow(row)