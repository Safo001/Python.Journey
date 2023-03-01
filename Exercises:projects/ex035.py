#I developed a program that read the value of 3 lines and answer if they are able to form a triangle.

l1 = float(input('Enter the first side:'))
l2 = float(input('Enter the second side:'))
l3 = float(input('Enter the third side:'))

if l1+l2>l3 \
        and l1+l3>l2 \
        and l3+l2>l1:
    print('This sides can form a triangle')
else:
    print('Thpse sides can not form a triangle.')

print('END!')