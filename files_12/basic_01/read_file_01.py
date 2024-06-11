# program to read from text files
"""
1- open file for reading
2- read content and use print to show the content
3- close file
"""
print('------ First way -----')
my_file = open('C:\\MY_FILES\\read_data.txt', 'r')
# print('this is \n\ta test')  # escape sequence
content = my_file.read()
print(content)
my_file.close()

print('---- Second way - using with ignore close() ----------')
with open('C:\\MY_FILES\\read_data.txt', 'r') as f:
    content = f.read()
    print(content)
