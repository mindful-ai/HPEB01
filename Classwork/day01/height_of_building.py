# Program to calculate the height of the object

import math

# Input

dist = float(input('Enter the distance in feet: '))
ang  = float(input('Enter the angle in degrees: '))

# Process

 height = dist * math.tan(math.radians(ang))

# Output

print('The height of the building is %.2f ft' % height)
