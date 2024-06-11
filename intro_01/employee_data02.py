# employee basic data
employee_id = 101                   # int data type
employee_name = 'Ahmed Amr'         # string data type
employee_salary = 7000.55           # float data type
employee_job = 'Python developer'   # string data type

print('------ Concat string to string -------')
print(employee_name + ' works as '+employee_job)

print('------ Concat string to int -----------')    # Ahmed Amr his id = 101
print('--- Convert data type from int to string ----- [ Casting ] ---')
print(employee_name + ' his id = ' + str(employee_id))

print('------ Concat string to float ---------')
print('--- Convert data type from float to string ----- [ Casting ] ---')
print(employee_name + ' takes salary = ' + str(employee_salary))

print('------- Convert from float to int --- [ Casting ] ---------')
print(employee_salary)
print(type(employee_salary))
print('---')
new_salary = int(employee_salary)
print(new_salary)
print(type(new_salary))