import random

print('------ random game calculator -------')
correct_answers = 0
wrong_answers = 0
for i in range(5):
    print('Question no. ', i + 1)
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    print(first_number, ' + ', second_number, ' = ')
    user_input = input()
    user_input = int(user_input)

    if user_input == first_number + second_number:
        print('Correct answer')
        correct_answers = correct_answers + 1
    else:
        print('Wrong answer')
        wrong_answers = wrong_answers + 1
    print('-----------------------')

print('end of program')
print('Correct answers = ', correct_answers)
print('Wrong answers = ', wrong_answers)