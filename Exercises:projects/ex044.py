price = float(input('How much is the product? £'))
print('The product price is {:.2}.'.format(price))

print('How would you like to pay for this product?\n'
                   '[1] Cash\n'
                   '[2] Card\n'
                   '[3] 2x on Card\n'
                   '[4] 3x or more on Card\n')
payment = int(input('Select your payment method:'))

if payment == 1:
    disc1 = price - ((10 * price) / 100)
    print('You will pay by cash, you have 5% discount. Final price {:.2f}.'.format(disc1))
elif payment == 2:
    disc2 = price - ((5 * price) / 100)
    print('You will pay by card, you have 10% discount. Final price {:.2f}.'.format(disc2))
elif payment == 3:
    tot = price/2
    print('You will pay by 2 x on card, so you will pay the original price of £{:.2f}.'.format(tot))
elif payment == 4:
    times = int(input('In how many instalments do you want?'))
    tot = (price/times) + (((20*price)/100)/times)
    print('You will pay in {} instalments, so you will pay with 20% interest.\n'
          'Final price £{:.2f}.'.format(times,tot))
else:
    print('\033[1;31;40mError: Invalid payment method!!!\033[m')