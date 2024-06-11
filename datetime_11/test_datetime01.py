# Here we will show all basic operations on datetime

# from datetime module import datetime class
from datetime import datetime
print('---- 1- get The current date and time ----')
today = datetime.now()
print(today)

print('---- 2- get only date or time or their parts ----')
print(today.date())
print(today.date().day)
print(today.date().month)
print(today.date().year)
print(today.date().weekday()) # which day in a week ? start by Monday = 0

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)

print('-- 3- Reformatting date, time ------ | we use strftime() function-----')
print('----- Convert date into String using strftime() function ------')
print(today)
print(today.strftime('%d-%m-%Y')) # day, month, year
print(today.strftime('%d-%m-%Y-%y-%W')) # day, month, year, yr, week per year
print(today.strftime('%B-%b-%A-%a')) # Month - Mon - Day - Dy
# timing format
print(today.strftime('%H-%M-%S')) # Hours 24 - Minutes - Seconds
print(today.strftime('%I-%M-%S %p')) # Hours 12 - Minutes - Seconds - AM|PM

print('---- 4- Create a custom date 21-September-2023 ------')
print('---- 1st way : datetime object using constructor -------')
#my_turtle = Turtle()    # my_turtle is object from class Turtle
custom_date = datetime(year=2023, month=9, day=21)
print(custom_date)

print('---- 2nd way : by converting a string into Date using strptime() function ----')
date_string_style = '21-9-2023' # String
new_custom_date = datetime.strptime(date_string_style, '%d-%m-%Y')
print(new_custom_date) # datetime

print('------------ 5- Comparison ------------')

if today.date() > custom_date.date():
    print('Today is newer than custom date')
elif today.date() < custom_date.date():
    print('Today is older than custom date')
else:
    print('2 dates are equal')
