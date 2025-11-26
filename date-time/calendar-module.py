# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month, day, year = map(int, input().strip().split())
weekday = calendar.weekday(year, month, day)
print(weekdays[weekday].upper())