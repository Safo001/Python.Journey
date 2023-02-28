'''I have made a program that read a year and shows if that year is a leap year or not.'''

year = int(input('What year you want to know?'))
print('The year you picked is {}.'.format(year))

if year % 4 == 0:
    print('It is a leap year. It has 366 days.')
else:
    print('It is not a leap year. It has 365 days.')
print('END!')