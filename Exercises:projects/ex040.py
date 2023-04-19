grade1 = float(input('What was your first grade?'))
grade2 = float(input("What was your second grade?"))
print('Your grades was {:.1f} Marks for the first assignment and {:.1f} Marks for the second!'.format(grade1,grade2))
avrg = (grade1 + grade2)/2

print("Your average Mark is {:.1f}.".format(avrg))
if avrg < 5:
    print('You have failed the module.')
#elif avrg > 5 and avrg <= 6.9:
elif 7 > avrg >= 5:
    print('You will take a resit in the summer!')
elif avrg >= 7:
    print('Congratulations, you have passed the module!')