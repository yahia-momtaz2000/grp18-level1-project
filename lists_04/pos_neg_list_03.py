
print('----- program to calculate pos, neg numbers sum and count ----------------')
numbers_list = [15, -16, 20, -3, 0, 20]

total_pos, total_neg, count_pos, count_neg, count_zeros = 0, 0, 0, 0, 0

for item in numbers_list:
    if item > 0: # item is positive
        total_pos = total_pos + item
        count_pos = count_pos + 1
    elif item < 0:  # item is negative
        total_neg = total_neg + item
        count_neg = count_neg + 1
    else:
        count_zeros = count_zeros + 1

print(total_pos, count_pos, total_neg, count_neg, count_zeros)
