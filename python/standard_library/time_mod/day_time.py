from datetime import datetime
import time

""" dt = datetime(2018, 1, 1)
print(dt)
datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")

time_me = datetime.fromtimestamp(time.time())
print(time_me) """


print(datetime.now())
dt = datetime(2018, 2, 4)
my_time = datetime.fromtimestamp(time.time())
print("This is my time :",my_time)
print(dt)


