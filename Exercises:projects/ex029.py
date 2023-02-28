'''I did create a program that read the speed of a car,
and if the car exceed 80km/h as speed this limit, show a message saying you were fined.
The fine costs £7 per each Km exceeded'''

import math

speed = float(input('What is the car speed?'))
print("You have passed that road at {:1}Km/h.".format(speed))
fine = 7 * (speed - 80)
if speed > 80:
    print('You have exceeded the speed limit.')
    print('You have to pay a fine of £{}.'.format(fine))
else:
    print('you are within the allowed speed.')
print("END.")