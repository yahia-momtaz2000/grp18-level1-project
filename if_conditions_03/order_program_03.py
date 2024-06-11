print('----- program to check for order discounts ----')
# inputs [ variables ]
item_cost = 500.0
item_qty = 3

special_client = 0    # 1 is special    |   0 is not special
# processing
total_order_cost = item_cost * item_qty
discount_pct = 0
if total_order_cost >= 1000:
    if special_client == 1:
        discount_pct = 20
    else:
        discount_pct = 10


discount_val = total_order_cost * discount_pct / 100

print('Total order cost before discount = ', total_order_cost)
total_order_cost = total_order_cost - discount_val
print('discount pct = ', discount_pct)
print('discount value = ', discount_val)
print('Total order cost after discount = ', total_order_cost)


