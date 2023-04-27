
sum_num = 0
numbers = []
for n in range (6):
    num = int(input(f'Enter the number #{n+1}:'))
    numbers.append(num)
    if num % 2 == 0:
        sum_num += num
print('The numbers are {}'.format(numbers))
print(f'The sum of those numbers is {sum_num}')