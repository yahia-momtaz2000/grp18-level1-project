# program to read from a file and write to another file

with open('C:\\MY_FILES\\read_data.txt', 'r') as f:
    content = f.read()

with open('C:\\my_files\\write_date2.txt', 'w') as f:
    f.write(content)