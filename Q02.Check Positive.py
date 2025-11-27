# To conver all the input to positive number


def isPositive(n:int)->int:
    if n<0:
        n=n*-1
        return n
    else:
        return n
    
print(isPositive(-21))