from calendar import month
import datetime

from datetime import date

dt = datetime.datetime.now()

# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.date())
# print(type(dt))

my_dt_string = "May 12 2022 11:14:10"

print(my_dt_string)
print(type(my_dt_string))

converted = datetime.datetime.strptime(my_dt_string, '%B %d %Y %H:%M:%S')

print(converted)
print(type(converted))


current_date = datetime.datetime.now()
print(current_date)
print(type(current_date))

#07/05/2022

dt_str = current_date.strftime('%d/%m/%Y')

print(dt_str)
print(type(dt_str))

d1 = date(year=2022,month=5,day=7)
d2 = date(year=2022,month=5,day=1)

print(d1-d2)

