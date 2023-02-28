import random
s1 = str(input("First student:"))
s2  = str(input('Second student:'))
s3 = str(input('Third student:'))
s4 = str(input('Fourth student:'))
'''students = [s1, s2, s3, s4]
random.shuffle(students)
print('The presentation order is:')
print(students)'''
sort = random.sample([s1, s2, s3, s4], k=4)
print('The presentation order is {}.'.format(sort))