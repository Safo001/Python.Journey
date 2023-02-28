wage = float(input('How much do you get paid annually: £'))
newwage = wage + (15*wage/100)
print("Initially you used to get paid £{:.2f} annually, however increasing 15% of your wage now you get paid £{:.2f} annulay.".format(wage,newwage))