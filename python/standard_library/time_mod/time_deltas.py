from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1) + timedelta(days=1,seconds=1)
dt2 = datetime.now()

print(dt1)
print(dt2)

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())

