Name = str(input('Full Name:')).strip( )
print('Your full name in capital letters is: {}'.format(Name.upper()))
print('Your full name in lower case is: {}'.format(Name.lower()))
print('Your full name has {} letters in total.'.format(len(Name) - Name.count(" ")))
Split = Name.split()
print('Your first name is {}, and has {} letters in total.'.format(Split[0],len(Split[0])))

