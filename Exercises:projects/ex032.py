'''I have made a program that read a year and shows if that year is a leap year or not.'''

from datetime import date
year = int(input('What year you want to know?'))

if year == 0:
    year = date.today().year
    print('The year you picked is {}.'.format(year))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #it is leap when is divisible by 100 and 400 simultaneously...
    print('It is a leap year. It has 366 days.')
else:
    print('It is not a leap year. It has 365 days.')
print('END!')