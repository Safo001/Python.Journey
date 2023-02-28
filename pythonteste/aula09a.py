phrase = '  I love my life  '
print(phrase.strip())
print(phrase.strip().replace('life',"girl"))
phrase = phrase.replace('life',"girl")
print(len(phrase))
print(phrase.count("l"))
print(phrase.lower().count('i'))
print(phrase.title().find('Love'))
print('girl' in phrase)

