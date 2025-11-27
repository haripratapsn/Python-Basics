# Finding Fibonacci Series

n=int(input("Enter n Number: "))
if (n==0):
    print(1)
elif (n==1):
    print(1,1)
else:
    a,b=1,1
    print(a,b,end=" ")
    for i in range(2,n+1):
        c=a+b
        print(c,end=" ")
        a,b=b,c
