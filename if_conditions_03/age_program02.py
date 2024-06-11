print('------- program to check for person age --------------')

person_age = input('Please enter your age : ')
person_age = int(person_age)            # casting : convert from string data type to int data type
print(person_age)
print(type(person_age))

"""
if person_age > 16:
    print('You are a man')
elif person_age >= 11 and person_age <= 16:
    print('You are a boy')
elif person_age >= 0:
    print('You are a child')
else:
    print('invalid age')
"""
if person_age > 16:
    print('You are a man')
elif person_age >= 11:
    print('You are a boy')
elif person_age >= 0:
    print('You are a child')
else:
    print('invalid age')
