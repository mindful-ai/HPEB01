import random

i = 0
L = []
while i < 100:
    L.append(random.randint(1, 100))
    i += 1  # i = i + 1

print('RAW')
print(L)

S = set(L)
UL = list(S)

print('\nRAW UNIQUE')
print(UL)

print('\nSORTED UNIQUE')
print(sorted(UL))
 
