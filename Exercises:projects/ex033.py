'''I wrote a program to compare numbers, and show which one is bigger and smaller'''

n1 = float(input('Ender the first number:'))
n2 = float(input('Ender the second number:'))
n3 = float(input('Ender the third number:'))
'''smaller = n1
bigger = n1
if n1<n2 and n1<n3:
    smaller = n1
if n3<n1 and n3<n2:
    smaller = n3
if n1>n2 and n1>n3:
    bigger = n1
if n3>n1 and n3>n2:
    bigger = n3
print('The larger number is {}.'.format(bigger))
print("the smaller number is {}.".format(smaller))'''
#Or I can write like:

numbers = [n1,n2,n3]
print('The larger number is {}.'.format(max(numbers)))
print('The smaller number is {}.'.format(min(numbers)))