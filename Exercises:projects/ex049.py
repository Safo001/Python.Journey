num = int(input('Enter a number:'))
print(f'Multiplication table of {num}:')
print('___'*10)
if num in range (1,13):
    for mul in range (1,13):
        res = num * mul
        print('{} x {} = {}'.format(num, mul, res))
else:
    print('Error!')
print("___"*10)
print('END!')