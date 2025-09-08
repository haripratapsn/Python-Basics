# To check whether the number is even or odd

def isEven(n:int)->None:
    res=n//2
    print(res)
    num=res*2
    print(num)
    if n==num:
        print(f'{n} is even')
    else:
        print(f"{n} is odd")

        
isEven(3)