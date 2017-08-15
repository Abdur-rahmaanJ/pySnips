#program to to find the calendar for a certain month
#visit abdurrahmaanjanhangeer.wordpress.com

import calendar
#iy = input('y .. ')
#im = input('m .. ')

year = 2016 # change to today's date
month = 6
cal = calendar.month(year, month)

print ("Here is the calendar of year {} and month {} of the year".format(year,month))
print()
print (cal)
