n = int(input("Enter a number: "))

'''
assume = 1

for d in range(2, n):
    if(n % d == 0):
        assume = 0
        break

if assume:
    print('This is a prime number')
else:
    print('This is not a prime number')

'''

for d in range(2, n):
    if(n%d==0):
        print('This is not a prime number')
        break
else:
    print('This is a prime number')
