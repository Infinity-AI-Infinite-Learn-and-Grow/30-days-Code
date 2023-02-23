import time 
import datetime
from time import ctime

print(time.strftime("%m:%d:%Y", time.localtime()))
print(time.strftime("%H:%M:%S", time.localtime()))


#time difference 
time_now = datetime.datetime.now()

new_year = datetime.datetime(time_now.year+1, 1, 1, 0, 0, 0)

time_diff= new_year - time_now
print(time_diff)