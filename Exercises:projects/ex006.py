import math
number = int(input('Enter a number:'))
double = number*2
triple = number*3
squareroot = math.sqrt(number)
# or squareroot = number**(1/2) or pow(number, (1/2))
print('The double of this number is {}, the triple is {}, and the square root is {:.3f}!'.format(double, triple, squareroot))