height = float(input("Height of the wall:"))
width = float(input("Width of the wall:"))
area = height * width
paint = area/2
print('This wall has the dimension {}x{}, it result in an area of {:.3f}m2.'.format(height,width,area))
print('To paint this wall, you will need {:.3f}L of paint.'.format(paint))