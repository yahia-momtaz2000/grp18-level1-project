
# function to find a number in list ; return its index or -1 if not found
# 2 parameters
def find_number(my_list, value):
    if value in my_list:
        return my_list.index(value)
    else:
        return -1


# main program
list1 = [12, 15, 6, 10, 9, 20]
v_result = find_number(list1, 10)
print(v_result)


