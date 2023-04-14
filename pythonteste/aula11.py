print("\033[7;33;44mHello World!\033[m")
a = 3
b = 4
sum = int(a) + int(b)
print('The sum of \033[1;31;42m{}\033[m and \033[1;34;45m{}\033[m is equal to \033[1;29;46m{}\033[m'. format(a,b,sum))

#Another Method
name = 'Leopold'
print('Nice to meet you, {}{}{}!!!'.format('\033[1:35m',name,'\033[m'))

#One More Method
name = 'Leopold'
colors = {'clear': '\033[m',
          'Red':'\033[31m',
          'Blue':'\033[34m',
          'Green':'\033[32m'}
print('Nice to meet you, {}{}{}!!!'.format(colors['Blue'],name,colors['clear']))

