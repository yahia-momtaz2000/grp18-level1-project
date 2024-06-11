# function to return True if it is even number or False if it is odd number
def check_number(value=10):
    if value % 2 == 0:
        return True
    else:
        return False


# main program
v_result = check_number(20)
if v_result:    # if v_result == True
    print('It is even number')
else:
    print('It is odd number')

# task : recode the same function by another 2 extra solutions