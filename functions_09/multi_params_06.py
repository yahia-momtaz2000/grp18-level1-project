
def add_numbers(*numbers_tuple):
    """
    this function used to get the total from all parameters
    :param numbers_tuple: variable parameter length - you can add any numbers of parameters here
    :return: total from all parameters
    """
    total = 0
    for item in numbers_tuple:
        total = total + item
    return total


# main program
print(add_numbers(5 , 6, 8, 10, 15, 17, 16, 12, 20, 1))

