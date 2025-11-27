# To Print digits in a integer value

def getDigit(n):
    while n>0:
        dig=n%10
        print(dig)
        n=n//10

getDigit(20)