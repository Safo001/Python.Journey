Name = str(input("What is your full name?")).strip()
n = Name.split()
print('Your first name is {}.'.format(n[0]))
print('your last name is {}.'.format(n[len(n)-1]))