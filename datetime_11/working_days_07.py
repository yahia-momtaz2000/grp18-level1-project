
# a program to get the date after 12 working days from a date ( ex. from today 18-5-2024 )  result # 3-6-2024
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
jump_days = 12
result_day = today
for i in range(jump_days):
    if result_day.date().weekday() == 3:  # Thursday
        result_day = result_day + relativedelta(days=3)
    elif result_day.date().weekday() == 4: # Friday ( check if today only is friday )
        result_day = result_day + relativedelta(days=2)
    else:
        result_day = result_day + relativedelta(days=1)

print('Result day = ', result_day)