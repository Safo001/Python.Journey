
greater = 0
smaller = 0
for p in range(0,5):
    weight = float(input('Enter the weight for the person #{} in Kg:'.format(p+1)))
    if p == 1:
        greater = weight
        smaller = weight
    else:
        if weight > greater:
            greater = weight
        if weight < smaller:
            smaller = weight

print(f'The gretest value is {greater}, and the amallest is {smaller}.')