# create a function to print numbers from 1 > N
def print_numbers(max_num):
    total = 0
    for i in range(1, max_num + 1):
        print(i, end=' ')
        total = total + i # to calculate summation of numbers from 1 to max_num
    return total        # return the function result to the main program

# main program
# call ( invoke ) the function
print('-- program to show user defined functions with parameters [ arguments ] and return sum of numbers -----')

v_result1 = print_numbers(10)
print()
print('The result from first call = ', v_result1)
v_result2 = print_numbers(20)
print()
print('The result from second call = ', v_result2)
v_result3 = print_numbers(30)
print()

print('The result from third call = ', v_result3)


