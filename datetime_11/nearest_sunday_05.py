# program to show the nearest sundays
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now() # 18-5-2024 ( SAT )

print('----- find the nearest sunday from today ----') # 19-5-2024 ( SUN )
nearest_sunday = today + relativedelta(weekday=calendar.SUNDAY) # 6
print(nearest_sunday)

print('------ find the nearest 2nd sunday from today -----') # 26-5-2024
nearest_2nd_sunday = today + relativedelta(weekday=calendar.SUNDAY, weeks=1)
print(nearest_2nd_sunday)

print('------ find the first sunday from the beginning of the current month -----')  # 5-5-2024

print('------ find the first sunday from the beginning of next month -----')  # 2-6-2024

print('------ find the first sunday from the beginning of the current year -----')  # 7-1-2024

print('------ find the first sunday from the beginning of next year -----')  # 5-1-2025