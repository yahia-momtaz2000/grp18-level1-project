print('---- validate complex password ------')

password = "sr@M@7_frtue$._"
upper_count, lower_count, digits_count, signs_count = 0, 0, 0, 0

if len(password) >= 8:
    # check for other points
    for letter in password:
        if letter.isupper():
            upper_count = upper_count + 1
        elif letter.islower():
            lower_count = lower_count + 1
        elif letter.isdigit():
            digits_count = digits_count + 1
        elif not letter.isalnum():
            signs_count = signs_count + 1
    # after end loop
    if upper_count > 0 and lower_count > 0 and digits_count > 0 and signs_count > 0:
        print('Password is Valid')
    else:
        print('Password is not Valid')
else:
    print('Password is Not Valid')
