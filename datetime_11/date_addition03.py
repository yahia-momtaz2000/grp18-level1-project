print('----- program to add, subtract 2 years, 5 months, 2 days to a date ----')

from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

# new_date = today + 5    # ERRRRORR

new_date = today + relativedelta(days=5, months=3, years=1)
print(new_date)