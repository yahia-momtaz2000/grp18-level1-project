
# function to return sum of even numbers from a list
def sum_even(my_list):
    total_even = 0
    for item in my_list:
        if item % 2 == 0:
            total_even = total_even + item
    return total_even


# main program
list1 = [5, 6, 10, 12, 16, 7]
v_result = sum_even(list1)
print('Sum of even numbers = ', v_result)
