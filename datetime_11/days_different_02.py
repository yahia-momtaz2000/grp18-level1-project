# from datetime module import datetime class
from datetime import datetime

# from relativedelta module found in dateutil pkg import relativedelta class
from dateutil.relativedelta import relativedelta

print('----- GEt the difference between 2 dates --------')

print('--- 1- get the difference between 2 dates in Days as a total ------------')

today = datetime.now()
custom_date = datetime(year=2024, month=3, day=10) # 10-March-2024
different_in_days = today - custom_date
# print(different_in_days)
print(different_in_days.days)

print('--- 2- get the difference between 2 dates in Years, Months, Days using relativedelta module ---')
# create object different_in_parts from class relativedelta using constructor  ()
different_in_parts = relativedelta(today, custom_date)
print(different_in_parts)
print(different_in_parts.years, different_in_parts.months, different_in_parts.days)
