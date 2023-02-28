from math import radians, cos, sin, tan
angle = float(input("Enter the angle:"))
print("For the angle {}º, the cosine is {:.2f}.".format(angle, cos(radians(angle))))
print("For the angle {}º, the sine is {:.2f}.".format(angle, sin(radians(angle))))
print("For the angle {}º, the tangent is {:.2f}.".format(angle, tan(radians(angle))))