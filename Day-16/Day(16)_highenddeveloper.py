
#Get the current day, month, year, hour, minute and timestamp from datetime module and print Format the current date using this format: ("%m/%d/%Y, %H:%M:%S") also Today is 20 February, 2023. Change this time string to time.

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Get the current day, month, year, hour, minute and timestamp from datetime module and print
today = datetime.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.hour)
print(today.minute)
print(today.timestamp())

# Format the current date using this format: ("%m/%d/%Y, %H:%M:%S")
print(today.strftime("%m/%d/%Y, %H:%M:%S"))

# also Today is 20 February, 2023. Change this time string to time.
print(today.strftime("Today is %d %B, %Y"))

# Change this time string to time.
time_string = '2021-01-01 00:00:00'
time_object = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
print(time_object)

