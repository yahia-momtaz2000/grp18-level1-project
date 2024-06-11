print('----------- program to calculate emp monthly, annual net salary ------------')
emp_id = 101
emp_name = 'Ahmed Farahat'
emp_gross_salary = 3000.0

if emp_gross_salary < 5000:
    tax = 0
else:
    tax = 10

emp_monthly_net_salary = emp_gross_salary - emp_gross_salary * tax / 100
print(emp_monthly_net_salary)

emp_annual_net_salary = emp_monthly_net_salary * 12
print(emp_annual_net_salary)
