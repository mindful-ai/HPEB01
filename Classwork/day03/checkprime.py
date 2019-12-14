def checkprime(N):
    for i in range(2, N):
        if(N % i == 0):
            return False
    return True


########################################

if __name__ == '__main__':
    
    x = int(input('Enter a number: '))
    res = checkprime(x)
    if(res):
        print('It is a prime number')
    else:
        print('It is not a prime nummber')
        

