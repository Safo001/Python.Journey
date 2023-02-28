'''I create a program that read the distance of a trip in km, and calculate the ticket price
the ticket cost £0.50 per Km for trips up to 200Km, longer trips tickets cost £0.45 per km.'''

price1 = 0.50
price2 = 0.45
print("Hello, welcome to Safo transportation,\nthe tickets prices vary form £{}/km for trips up to 200km,\nand £{}/km for longer trips!".format(price1,price2))

distance = float(input('What is the trip distance?'))
print("Your trip distance is {}Km.".format(distance))
ticket1 = float(price1 * distance)
ticket2 = float(price2 * distance)

if distance <= 200:
    print("Your ticket will cost £{}.".format(ticket1))
else:
    print("Your ticket will cost £{}.".format(ticket2))
print("Thank you for the preference, have a nice journey!")
