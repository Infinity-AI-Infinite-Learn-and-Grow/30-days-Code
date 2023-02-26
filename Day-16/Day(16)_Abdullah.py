# 1. Get the current day, month, year, hour, minute and timestamp from datetime /
# module and print Format the current date using this
# format: ("%m/%d/%Y, %H:%M:%S") also Today is 20 February, 2023.
# Change this time string to time.
# 2. Calculate the time difference between now and new year.

# ---Task 1----
import datetime
import time
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Current Day, Month, Year, Hour, Minute and Timestamp =", dt_string)

# ----Task 2----
str_d1 = now.strftime("%Y/%m/%d")
str_d2 = '2024/01/01'

d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

delta = d2 - d1
print('Difference is {} days'.format(delta.days))
