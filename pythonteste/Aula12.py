name = str(input("What is your name?"))
if name == 'Leopold':
    print("What a beautiful name!")
elif name == 'John' or name == 'Marie' or name == 'Hanna':
    print('Your name is really common in the UK.')
elif name in "LSian Anisa Jessica Monica":
    print('That is a beautiful female name!')
else:
    print('You have a normal name.')
print('Have a good day {}!'.format(name))