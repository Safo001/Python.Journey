inprice = float(input('The initial price of this product: £'))
discount = (5*inprice)/100
finprice = inprice - discount
print('This product that was £{:.2f} last month, with 5% discount it costs now £{:.2f}.'.format(inprice,finprice))