print('----- program to merge 2 lists to create a new dictionary ------')

emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

person_dict = {}

for i in range(len(emp_ids_list)):
    person_dict[emp_ids_list[i]] = emp_names_list[i]      # adding

print(person_dict)
