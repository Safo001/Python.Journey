num1 = int (input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print('The numbers you did choose are:\n'
      '\033[1;31m{}\033[m and \033[1;31m{}\033[m!'.format(num1,num2))
if num1 > num2:
    print('The first number({}) is greater that the second one({})!'.format(num1,num2))
elif num1 < num2:
    print('The second number({}) is greater than the second one({})!'.format(num2,num1))
else:
    print("There is not greater number, they are both equals.")