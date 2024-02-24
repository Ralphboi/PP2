#1
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date five days ago:", new_date)


#2
from datetime import datetime, timedelta
current_date = datetime.now()
yd = current_date - timedelta(days=1)
tmrw = current_date + timedelta (days=1)

print("Current Date:", current_date)
print("Yesterday:", yd)
print("Tommorow:", tmrw)


#3
from datetime import datetime
current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)

#4
from datetime import datetime

date1 = datetime(2023, 5, 15, 12, 30, 15)
date2 = datetime(2023, 5, 10, 8, 45, 30)
time_difference = date1 - date2
difference_in_seconds = time_difference.total_seconds()

print("Difference between the two dates in seconds:", difference_in_seconds)
