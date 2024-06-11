print('--- program to remove signs from a string ------')

statement = "123abcjw:, .@! eiw"
new_statement = ''
for letter in statement:
    if letter.isalnum():
        new_statement = new_statement + letter   # concat

print(new_statement)
statement = new_statement
print(statement)
