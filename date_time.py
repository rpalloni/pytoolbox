import time
time.time() # number of seconds since the Unix epoch 01/01/1970 00:00:00 GMT Greenwich Mean Time

from datetime import date, time, datetime
date(year=2020, month=1, day=31)

time(hour=13, minute=14, second=31)

datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)

today = date.today()
today

now = datetime.now()
now

current_time = time(now.hour, now.minute, now.second)
datetime.combine(today, current_time)

# ISO: all dates should be written in order of most-to-least-significant data YYYY-MM-DD HH:MM:SS
date.fromisoformat("2020-01-31")

date_string = "01-31-2020 14:45:30"
format_string = "%m-%d-%Y %H:%M:%S"
datetime.strptime(date_string, format_string)

date_string = "01-31-2020 14:45:30"
format_string = "%d-%m-%Y%H:%M:%S"
datetime.strptime(date_string, format_string)

today.strftime("%Y-%m-%d")
today.strftime("%d-%m-%Y")

# django template date format [db: yyyy-mm-dd]
#  <input type="date" class="form-control" name="year" value="{{ birthdate|date:"Y-m-d" }}">