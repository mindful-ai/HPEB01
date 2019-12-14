# Program to calculate the area and circumference
# of a circle

import math

# Input
rad = float(input('Enter radius of the circle: '))

# Process

area = math.pi * math.pow(rad, 2)
circ = 2 * math.pi * rad

# Output

print('AREA           : ', area)
print('CIRCUMFERENCE  : ', circ)
