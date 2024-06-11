
print('--- program to reverse words of string -----')

statement = "i like this program very much"

# statement = statement[::-1] # reverse letters  [ wrong answer ]

# convert string to a list using split()
words_list = statement.split()
words_list.reverse()
print(words_list)

# Convert the list back to string
statement = ' '.join(words_list)
print(statement)
