n1 = float(input("What was your second mark?"))
n2 = float(input("What was your first mark?"))
m = (n1+n2)/2
print ('Your overal mark was {}.'.format(m))
if m >= 40:
    print('Congratulations, you have passed the module!')
else:
    print("I am sorry, you have to retake this module exam this summer!")