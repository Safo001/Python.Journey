
num = int(input('Enter a number:'))

for p in range(1,num):
   if num % p == 0 and num % num == 0:
        print(f'{num} is a prime number!')