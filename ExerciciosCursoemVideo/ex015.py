days = int(input('How many days the car was rented:'))
distance = float(input('How many Km it was drive:'))
payment = days * 60 + distance * 0.15
print('The total to be paid is £{:.1f}'.format(payment))
