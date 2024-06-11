print('---- program to generate a unique list and another duplicate list for elements ----')

numbers_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
unique_list = []        # [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
duplicate_list = []     # [ 1, 2, 5, 9]

# Loop [ for i index - for each item ]  :> for each item
for item in numbers_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicate_list:
        duplicate_list.append(item)

print(numbers_list)
print(unique_list)
print(duplicate_list)