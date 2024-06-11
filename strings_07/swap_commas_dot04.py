print('---- swap dots and commas -----')

statement = 'He is Ahmed, Ahmed lives in cairo, Ahmed plays football.'

statement = statement.replace(',', '_')   # put a temp sign


statement = statement.replace('.', ',')


statement = statement.replace('_', '.')

print(statement)