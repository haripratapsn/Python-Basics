# Factorial

def getFactorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)

getFactorial(3)