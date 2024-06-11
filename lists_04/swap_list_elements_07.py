print('--- Swap the first and last element of the list ----')
numbers_list = [12, 35, 9, 56, 24]

var_temp = numbers_list[0]              # 12
numbers_list[0] = numbers_list[-1]      # [24, 35, 9, 56, 24]
numbers_list[-1] = var_temp

print(numbers_list)
