
print('All odd numbers between 1 and 500 that are divisible by 3 are:')

sum_of_odds = 0
for o in range(1,500,2):
    if o % 3 == 0:
        print(o)
        sum_of_odds += o
print(f'The sum of all numbers is {sum_of_odds}!')
print("END!")
