shopping_cart_dict = {'eggs': 160.0, 'milk': 40.0, 'bread': 20.0}

print('----- 1. Loop over a dictionary using for each loop ----- show all keys ----')
for key in shopping_cart_dict:
    print(key, shopping_cart_dict[key])

print('----- 2. Loop over a dictionary using for each loop ----- show all keys , values ----')
for key, value in shopping_cart_dict.items():
    print(key, value)