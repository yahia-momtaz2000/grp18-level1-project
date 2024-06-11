print('--- program to print 10 * 10 multiplication table ---')

for i in range(1, 11):      # rows
    for j in range(1, 11):  # columns
        if i * j < 10:
            print(i * j, end='  ')
        else:
            print(i * j, end=' ')
    print()  # Enter ( new line )


