import random
s1 = str(input("First student:"))
s2  = str(input('Second student:'))
s3 = str(input('Third student:'))
s4 = str(input('Fourth student:'))
students = [s1, s2, s3, s4]
sort = random.choice(students)
print('The student sorted is {}.'.format(sort))
