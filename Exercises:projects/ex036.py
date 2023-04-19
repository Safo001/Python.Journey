#A program to approve a mortgage based on the house price, monthly income, and mortgage time
#as long as the the monthly payment doe not exceed 30% of the monthly income!

name = str(input('Hello, What is your name?'))
print('Welcome to UK Bank {}, to proceed your mortgage I will need to collect some information:\n'
      'The house price, your monthly income and how many years you do intend to pay for it please!!\n'.format(name))

hprice = float(input('What is the total house price? £'))
wage = float(input('What is your monthly income? £'))
years = int(input('In how many years do you expect to pay the mortgage?'))

mpay = (hprice)/(years*12)
percent = (30*wage)/(100)

if mpay <= percent:
    print('Your mortgage application was accepted {}!\n'
          'You will pay \033[1;32m£{}\033[m every month during \033[1:34m{}\033[m years!\n'.format(name,mpay,years))
elif mpay > percent:
    print('Unfortunately your application was denied {},\n'
          'your credit score does not meet the requirements,\n'
          'as the monthly payment is {} and exceed 30% of your monthly income.\n'.format(name,mpay))
else:
    print('We were unable to check your data, come back another day {}!'.format(name))
print('Thank you for the preference, see you soon!!')