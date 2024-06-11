print('---- program to show dictionary operations ------------')

# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart_dict = {'eggs': 160.0, 'milk': 40.0, 'bread': 20.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict))

print('------ Adding, change new pair to the dictionary -------')
shopping_cart_dict['Nescafe'] = 40.5        # adding
shopping_cart_dict['milk'] = shopping_cart_dict['milk'] + 20        # change
print(shopping_cart_dict)


print('------ access element -----')
print('price of bread ', shopping_cart_dict['bread'])


print('---- delete element pair from dict ------')
shopping_cart_dict.pop('bread')
print(shopping_cart_dict)

