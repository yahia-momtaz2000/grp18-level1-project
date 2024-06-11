# program to read from excel [ csv ] and write back as output or put to list
import csv

people_list = []
with open('C:\\MY_FILES\\people.csv', 'r') as my_file:
    reader_list = csv.reader(my_file)
    for row in reader_list:
        people_list.append(row)

print(people_list)
print(people_list[2][2])