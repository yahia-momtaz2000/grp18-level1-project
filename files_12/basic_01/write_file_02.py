# program to write into text file
"""
1- open for write
2- operation ( write )
3- close file
"""

print('----- First way ------')
my_file = open('C:\\my_files\\write_date.txt','w')
my_file.write('I like programming\n')
my_file.write('I Like football\n\n')
my_file.write('Python is a programming Language')
my_file.close()

print('--------- Second way --------')
with open('C:\\my_files\\write_date.txt','a') as f:
    f.write('\n++++++++++++++++++++++++\n')
    f.write('Python is the basic programming for AI\n')
    f.write('You should learn DJango for Python backend development')
