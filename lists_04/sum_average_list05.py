print('---- program to get sum, average numbers is a list ---')
numbers_list = [15, 16, 20, 3, 15, 20]

# Loop  [ for i - for each ]
total = 0
for item in numbers_list:
    total = total + item

print('Total = ', total)

average = total / len(numbers_list)
average = round(average, 2)
print('Average = ', average)
