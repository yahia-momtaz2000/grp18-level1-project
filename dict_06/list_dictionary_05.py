
print('----- program to show list of dictionaries --------')

students_list = [{101: 'Ahmed', 102: 'Marwa', 103: 'Mostafa'}]

print(len(students_list)) # 1

print(students_list[0]) # {101: 'Ahmed', 102: 'Marwa', 103: 'Mostafa'}

print(students_list[0][102]) # Marwa

# Marwa > Marwa Mahmoud
students_list[0][102] = 'Marwa Mahmoud'
print(students_list)

print('------------')
students_dict2 = {104: 'Ayman', 105: 'Ibrahim'}
students_list.append( students_dict2 )
print(students_list)

print(students_list[1][105]) # Ibrahim

