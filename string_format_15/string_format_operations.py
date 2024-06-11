
# Show all printing options

client_id = 101
client_name = 'Ahmed Omar'
client_invoice = 78965.6782123

# Client has id = 101, his name is Ahmed Omar, his invoice value = 78965.6782123
print('------ 1- print with concat -----')
print('Client has id = ' + str(client_id) + '\n\t, his name is '+ client_name+', his invoice value = ', str(client_invoice))


print('------ 2- print with multi parameters --------')
print('Client has is = ', client_id, ', his name is ', client_name, ', his invoice value = ', client_invoice)


print('------ 3- String formatting using placeholders ---- %s %d %f ---- ')
print('Client has id = %d, his name is %s, his invoice value = %.2f' %(client_id, client_name, client_invoice))


print('----- 4- String Formatting using Format function -----')
print('Client has id = {:d}, his name is {:s}, his invoice value = {:,.2f}'.format(client_id, client_name, client_invoice))

print('----- 5- String Formatting using F-String function -----')
print(F'Client has id = {client_id}, his name is {client_name}, his invoice value = {client_invoice:,.2f}')

