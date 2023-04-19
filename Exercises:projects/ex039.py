from datetime import date
name = str(input('What is your name?'))
birth = int(input('In what years you were born?'))
date= date.today().year
age = date - birth
gender = str(input('What is your gender (M/F)?'))
G = gender.strip().lower()

years_left = 17 - age
years_past = age - 35

if G == 'f':
    print('You do not need to list to the army, since you are a woman!')
else:
      print('\033[4:29:40m{}\033[m Born in \033[4;29;40m{}\033[m!\n'
            'Actual age: \033[4:29:40m{}\033[m!'.format(name, birth, age))
if G == 'm' and age > 17 and age <= 35:
      print('You still on time to get listed to the army {}.'.format(name))
elif G == 'm' and  age == 17:
      print('It is time to list your name to the army {}.'.format(name))
elif G == 'm' and age > 35:
      print('You are {}y over the age limit to join the army unfortunately.'.format(years_past))
elif G == 'm' and age < 17:
      print('You still under the age to join the army {}.\n'
            'it left {}y so you will be able to join.'.format(name,years_left))
