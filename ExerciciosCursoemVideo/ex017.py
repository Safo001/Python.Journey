'''from math import sqrt, pow
opp = float(input("Enter the opposite:"))
adj = float(input("Enter the adjacent:"))
hip = sqrt(pow(opp, 2) + pow(adj, 2))
print('The hypotenuse will measure {:.2f}.'.format(hip))'''

import math
opp = float(input("Enter the opposite:"))
adj = float(input("Enter the adjacent:"))
hip = math.hypot(opp,adj)
print('The hypotenuse will be {:.2f}.'.format(hip))
