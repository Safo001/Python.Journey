'''I did create a program that makes the computer think of an integer between 0 and 5
and asks the user to try to discover this number chosen by the computer.
If the user gets it right, the program will write that he won, otherwise it will write that he lost.'''

import random
numbers = [0,1,2,3,4,5]
sort = random.choice(numbers)
pick = int(input('What was the number choosed by the computer?'))
if pick == sort:
    print('You won champ!')
else:
    print('You lost, the number picked by the computer was {}!'.format(sort))

#Or use PC = randint(0,5)
