import math     # call math module  || to use pow() function

print('---- program to calculate area, perimeter of circle ------')
# input :  PI | radius
# output : Area | Perimeter

radius = 7
PI = math.pi

perimeter = 2 * PI * radius

area = PI * math.pow(radius, 2)

print('perimeter = ', perimeter)
print('area = ', area )

print('perimeter = ', round(perimeter, 2) )
print('area = ', round(area, 2) )
