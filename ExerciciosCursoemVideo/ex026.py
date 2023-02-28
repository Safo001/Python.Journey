Phrase = str(input('Enter your phrase:')).strip().upper()
print('The letter A appears {} times. '.format(Phrase.count("A")))
print('The first time we have the letter A is in the position {}.'.format(Phrase.find("A")+1 ))
print('The letter A appears for the last time in the position {}.'.format(Phrase.rfind("A")+1))