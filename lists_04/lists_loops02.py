
print('----- 1 Loop over elements of a list using for i index Loop -----')
numbers_list = [14, 20, 5, 16, 10]
total = 0
for i in range( len(numbers_list) ):
    print(i, numbers_list[i] )
    total = total + numbers_list[i]

print('Sum = ', total)


print('---------- 2- Loop over elements of a list using for each Loop -------------')
total = 0       # reset variable
for item in numbers_list:
    print(item)  # numbers_list[i]
    total = total + item

print('Sum = ', total)

print('---------------------------------------')

print('Sum = ', sum(numbers_list) )      # builtin function
