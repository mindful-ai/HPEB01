import random

def genrandom(n = 20, s = 1, e = 100):
    rn = []
    for i in range(n):
        rn.append(random.randint(s, e))

    return rn

##########################################

randoms = genrandom(n = 100)
print('RANDOMS:')
print(randoms)

import checkprime

primes = []
for num in randoms:
    if(checkprime.checkprime(num)):
        primes.append(num)

print('PRIMES:')
print(primes)
