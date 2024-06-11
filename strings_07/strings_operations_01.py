# show strings functions
print('---- Create and print string ----')
emp_name = 'Yahia Momtaz'
print(emp_name)
print(type(emp_name))

print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name)  # Yahia Momtaz
print(upper_emp_name) # YAHIA MOMTAZ
print(lower_emp_name) # yahia momtaz


print('------ isupper(), islower(), isalpha(), isalnum(), isDigit() functions --- True , False --')
print(upper_emp_name.isupper()) # True
print(lower_emp_name.islower()) # True
print(emp_name.isupper()) # False
print(emp_name.isalpha()) # False
emp_code = '101'
print(emp_code.isalpha()) # False
print(emp_code.isdigit()) # True
emp_code = '101abc'
print(emp_code.isalnum()) # True


print('-------------- endsWith() function -----------------')
file_name = 'egypt.PdF'
file_name = file_name.lower() # to make the name and extension small [ egypt.pdf ]
if file_name.endswith('pdf'):
    print('it is a book')
elif file_name.endswith('mp3') or file_name.endswith('wav'):
    print('it is a song')
else:
    print('Unknown type')


print('-------------- startswith() function ---------')
emp_mobile = '01547041564'
if emp_mobile.startswith('010'):
    print('it is vodafone')
elif emp_mobile.startswith('011'):
    print('it is etisalat')
else:
    print('unknown mobile')


print('------ in membership ----- To find a word in a string ---------')
emp_cv = 'iam a programmer, iam interest in python java c++'

if 'python' in emp_cv and 'java' in emp_cv:
    print('it is the wanted emp')
else:
    print('it is not the wanted emp')


print('-------------- count function -----------')
emp_cv = 'iam a programmer, iam interest in python java c++, iam professional in python'
emp_cv = emp_cv.lower()
print('python keyword occurs times ', emp_cv.count('python'))


print('---------- index(),  replace() functions |  slicing ---------------')
emp_email = 'yahia.mostafa.aly@gmail.com'
print(emp_email.index('@'))
user_name = emp_email[0:  emp_email.index('@') ]
print('user name =', user_name)
domain_name = emp_email[emp_email.index('@') + 1:]
print('domain name = ', domain_name)

# change username , replace .  with space
user_real_name = user_name.replace('.',' ')
print(user_real_name)

print('--------------- Looping :  Loop over letters of string -----------------------')
print('---- for each loop -----')
for letter in emp_email:
    print(letter)

print('-- for i index loop ----')
for i in range(len(emp_email)):
    print(emp_email[i])


print('------ Split() function to split words of a string into a list of words ------')
student_name = 'java python oracle linux network'
courses_list = student_name.split()
print(courses_list)
for course in courses_list:
    print(course)

print('------ return the list back to string using join() function --------')
courses_list.reverse()
new_courses =  ' '.join(courses_list)
print(new_courses)


print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')
my_courses = 'java python oracle linux python network'
print(my_courses.find('python')) # first occurrence
print(my_courses.rfind('python')) # last occurrence

student_name = ' Marwan '
print(student_name)
student_name = student_name.strip()
print(student_name)