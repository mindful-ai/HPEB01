start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))

primes = []

for num in range(start, end + 1):

    for d in range(2, num):
        if(num%d==0):
            break
    else:
        primes.append(num)


print('PRIMES')
print(primes)
