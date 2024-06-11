print('---- program to show complex formula ------')
# inputs = x, y, a, b, c
# output = final_result

x, y, a, b, c = 2, 3, 4, 5, 6
part1 = (3 + 4 * x) / 5

part2 = (10 * (y - 5) * (a + b + c)) / x

part3 = 9 * (4 / x + (9 + x) / y)

final_result = part1 - part2 + part3
print('Final result = ', final_result)