number = int(input('Enter a number:'))
print('''Pick one of the convertions:
[1] Convert to Binary
[2] Convert to Octal
[3] Convert to Hexadecimal''')
option = int(input('Your option:'))

if option == 1:
    print('{} converted to birnary is {}.'.format(number, bin(number)[2:]))
elif option == 2:
    print("{} converted to octal is {}.".format(number, oct(number)[2:]))
elif option == 3:
    print('{} converte d to hexadecimal is {}.'.format(number, hex(number)[2:]))
else:
    print('Invalid Option, try again!')
