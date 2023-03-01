#I wrote a program that ask for the salary of an employee and calculate the pay rise.
#For salaries above £2500 the pay rise is in 10%
#For salaries below that value the pay rise is 15%

name = str(input('What is your name?'))
wage = float(input("What is your hourly pay? £"))
hours = float(input('How many hours per week do you work?'))
week = wage * hours
month = 4 * week
salary = month
print('Currently you get paid £{} a month.\nHowever, due to your hard work we decide to increase your wage.'.format(month))

rise1 = ((10 * salary)/100) + salary
rise2 = ((15 * salary)/100) + salary

#1 moth has 4 weeks, each week has certain hours of work, get the hourly pay
Hrise1 = rise1/(4 * hours)
Hrise2 = rise2/(4 * hours)
if salary <= 2500:
    print("Your hourly pay will be increased to £{}.".format(Hrise2))
    print("So you will start getting paid £{} a month.".format(rise1))
else:
    print('Your hourly pay will be increased to £{}.'.format(Hrise1))
    print("So you will start getting paid £{} a month.".format(rise1))

print("Thanks for your hard work {}.".format(name))
