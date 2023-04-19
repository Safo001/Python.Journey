height = float(input('Enter your height in meters:'))
weight = float(input('Enter your weight in kilograms:'))
print('You are {} tall, and weighting {}kg.'.format(height,weight))
#sq = pow(height,2)
#height**2
#math.pow(height,2)
BMI = (weight) / pow(height,2)
print('Your BMI is: {:.1f}.'.format(BMI))

if BMI < 18.5:
    print('You are under your ideal weight!')
elif BMI >= 18.5 and BMI < 25:
    print('You are within your ideal weight!')
elif BMI >= 25 and BMI < 30:
    print('You are over your ideal weight!')
elif BMI >= 30 and BMI < 40:
    print('You are within the Obesity group!')
else:
    print('You are withing the Morbid Obesity group!')