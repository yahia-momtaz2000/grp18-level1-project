
# program to show how to handle exceptions [ runtime errors ]
try:
    first_number = int( input('please enter first number : ') )
    second_number = int( input('please enter second number : ') )

    result = first_number / second_number
    print('Result = ', result)

    open('C:\\my_files\\egypt.txt')
except ValueError as e:
    print('Please enter only numbers', e)
except ZeroDivisionError as e:
    print('Cannot divide vy Zero', e)
except Exception as e:
    print('There is something wrong - please contact administrator', e)
finally:
    print('This is the finally section - must be executed')

print('---- Continue or End the program -----')

