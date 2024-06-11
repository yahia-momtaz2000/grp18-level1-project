# Using Lists
print('---- 1. Creating, Printing List ---- ')
numbers_list = [14, 20, 5, 16, 10]
print(numbers_list)
print(type(numbers_list))

print('---- 2. adding element to list [ append function , insert function ] --- ')
numbers_list.append(17)
print(numbers_list)
numbers_list.insert(2, 15)
print(numbers_list)

print('---- 3. Access element by index and change it -----')
print( numbers_list[4]  )
numbers_list[4] = numbers_list[4] + 5  # change the element value
print(numbers_list)


print('----- 4. count elements of list _ Len function : General Function -------')
print( len(numbers_list)   )


print('-------- 5. delete element from the list -- remove() , pop() functions -----')
numbers_list.remove(21) # by value
numbers_list.pop(2)     # by index
numbers_list.pop()      # remove last index
print(numbers_list)


print('-------- 6. reverse list ----------')
numbers_list.reverse()
print(numbers_list)


print('------- 7. sort list -------------')
numbers_list.sort()  # sort asc
print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list)
