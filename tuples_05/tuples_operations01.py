print('----- main tuple operations -------')

print('---- create and print tuple -----')
my_tuple = (101, 'Ahmed Mahfouz', 8000.0, 'Nasr city - Cairo')
print(my_tuple)
print(type(my_tuple))

print('---------- access element in a tuple by index [] -------------')
# nasr city - cairo
print(my_tuple[3])
# my_tuple[3] = 'Maadi'     Error
# print(my_tuple)

print('------------ un packing tuple ----- ')
person_id, person_name, person_salary, person_address = my_tuple
print(person_name, person_address)

print('------ Loop over Tuple -------')
for i in range(len(my_tuple)):
    print(my_tuple[i])
print('------')
for item in my_tuple:
    print(item)