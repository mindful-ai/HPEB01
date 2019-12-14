# Program to subtract two numbers

# Input
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Process

res = a - b

# Output

print('DIFFERENCE : ', res)
if(res > 0):
    print('The result is Positive')
elif(res < 0):
    print('The result is Negative')
else:
    print('The result is Zero')
