

def isPrime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def nextPrime(n):
    nextprime=n+1
    while True:
        if isPrime(nextprime):
            return nextprime
        nextprime+=1

        
print(nextPrime(15))