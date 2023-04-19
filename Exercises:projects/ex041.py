from datetime import datetime
birth = int(input('Enter your year of birth:'))
date = datetime.today().year
age = date - birth
print('Your were bort in {}!\n'
      'Your are {}yo\nSo your football category is:'.format(birth, age))
if age <= 9:
    print('Under 9yo!')
elif age > 9 and age <= 14:
    print('Under 14yo!')
elif age > 14 and age <= 19:
    print('Junior - Under 19yo!')
elif age >19 and age <= 25:
    print('Senior - Under 20yo')
else:
    print('Master - Over 25yo!')
