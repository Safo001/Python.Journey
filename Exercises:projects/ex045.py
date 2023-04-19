from random import randint, choice
from time import sleep
"""mypick = str(input('Rock, Paper or Scissor?')).capitalize()
print('{}.'.format(mypick))
game = ['Rock','Paper','Scissor']
pc = random.choice(game)
print('{}.'.format(pc))

if mypick == 'Rock'and pc == 'Paper'\
        or mypick == 'Paper' and pc == 'Scissor'\
        or mypick == 'Scissor' and pc == 'Rock':
    print('You lost the game!')
elif mypick == 'Rock' and pc == 'Scissor'\
        or mypick == 'Paper' and pc == 'Rock'\
        or mypick == 'Scissor' and pc == 'Paper':
    print('You won the game!')
elif mypick == pc:
    print('It is a Draw!')

print("GAME OVER!!!")"""

#or I can do this way
itens = ('Rock', 'Paper', 'Scissor')
pc = randint(0,2)
print('''Your options:
      [0] Rock!
      [1] Paper! 
      [2] Scissor''')
pick = int(input('Rock, Paper or Scissor?'))
print('Rock')
sleep(1)
print('Paper')
sleep(1)
print('Scissor')
sleep(1)
print('-='*11)
print('You played {}'.format(itens[pick]))
print('The computer played {}'.format(itens[pc]))
print('-='*11)

if pc == 0:
    if pick == 0:
        print('It is a Draw')
    elif pick == 1:
        print('PC Won.')
    elif pick == 2:
        print('You Won.')
    else:
        print('\033[1;31;40mError: Invalid Option!!!\033[m')
elif pc == 1:
    if pick == 0:
        print('PC Won.')
    elif pick == 1:
        print('it is a Draw')
    elif pick == 2:
        print('You Won.')
    else:
        print('\033[1;31;40mError: Invalid Option!!!\033[m')
elif pc == 2:
    if pick == 0:
        print('PC Won.')
    elif pick == 1:
        print('You Won.')
    elif pick == 2:
        print('it is a Draw.')
    else:
        print('\033[1;31;40mError: Invalid Option!!!\033[m')