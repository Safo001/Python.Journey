
a1 = int(input('Enter the first term:'))
d = int(input('Enter the common difference:'))
numbs =[]
for n in range (1,11):
    an = a1 + (n-1)*d
    numbs.append(an)
print(f'The first 10 terms of this arithmetic sequence is: {numbs}')
