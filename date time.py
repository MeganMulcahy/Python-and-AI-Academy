import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.timestamp()
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

new_year = datetime(2026,1,1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

# %a = Weekday, short = Wed
# %A = Weekday, long = Wednesday
# %w = Weekday as a number = 3
# %d = Day of Month 01-31 = 31
# %b = Month name, short = Dec
# %B = Month name, long = December
# %m = Month as a number = 12
# %y = Year, short = 26
# %Y = Year, long = 2026
# %H = Hour 00-23 = 17
# %I = Hour 00-12 = 05
# %p = AM/PM
# %M = Minute 00-59
# %S = Second 00-59
# %f = Microsecond 000000-999999
# %z = UTC offset = +0100
# %Z = Timezone = CST
# %j = Day number of year 001-366 = 365
# %U = Week number of year, Sunday as first day of week, 00-53 = 52
# %W = Week number of year, Monday as first day of week, 00-53 = 52
# %c = Local version of date and time = Mon Dec 31 17:41:00 2018
# %x = Local version of date = 12/31/18
# %X = Local version of time = 17:41:00
# %% A % character = %

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date object: ", date_object)

from datetime import date
a = date(2026, 1, 1)
print(a)
print('Current date:', a.today())
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

from datetime import time
a = time()
print("a =", a)
b = time(10, 30, 50)
print("b =", b)
c = time(hour=10, minute=30, second=50)
print("c =", c)
d = time(10, 30, 50, 200555)
print("d =", d)

from datetime import date, datetime
today = date.today()
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

# .isoweekday(): Returns the day of the week as an integer (1 = Monday, 7 = Sunday).
# .weekday(): Returns the day of the week as an integer (0 = Monday, 6 = Sunday).