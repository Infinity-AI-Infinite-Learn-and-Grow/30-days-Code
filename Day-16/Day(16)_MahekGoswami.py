#Day 16
from datetime import datetime

# -------Task 1-------
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# -------Task 2-------
str_d1 = '2023/02/20'
str_d2 = '2024/01/01'

d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

delta = d2 - d1
print('Difference is {} days'.format(delta.days))



