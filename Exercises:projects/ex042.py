l1 = float(input('Enter the first side:'))
l2 = float(input('Enter the second side:'))
l3 = float(input('Enter the third side:'))

if l1+l2>l3 \
        and l1+l3>l2 \
        and l3+l2>l1:
    print('This sides can form a triangle ', end='')
    if l1 == l2 == l3:
        print('Equilateral.')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2:
        print('Isoceles.')
    elif l1 != l2 != l3 != l1:
        print('Scalene.')
else:
    print('Those sides can not form a triangle.')

print('END!')