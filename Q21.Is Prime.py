# To check if the number is prime number

def isPrime(n):
    if n==0 or n==1:
        return False
    count=2
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    if count==2:
        return True
    else:
        return False
    
print(isPrime(89))