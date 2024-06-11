# program to find element in a list if found : print it is found in index
# - if not found print element is not found
# using No Flag

my_list = [15, 14, 10, 16, 20]
num = 11

for item in my_list:
    if item == num:
        print('number is found at index = ', my_list.index(num))
        break
else: # execute if loop complete without break
    print('number is not Found')