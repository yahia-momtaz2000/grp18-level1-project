print('--- program to find element in list ------')

my_list = [2, 4, 7, 12, 14, 6]
num = 7

is_found = False        # boolean    Flag
for i in range( len(my_list) ):
    if num == my_list[i]:
        print(num, ' is found at index = ', i)
        is_found = True

if not is_found:        # is_found == False
    print(num, ' is not found in the list')