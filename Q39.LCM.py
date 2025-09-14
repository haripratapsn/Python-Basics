# to find LCM
# LCM will be either multiplication of two numbers or less than the multiplication of the two numbers

a=int(input("Enter a Number: "))
b=int(input("Enter b Number: "))
res=max(a,b)
while (res<=a*b):
    if (res%a==0 and res%b==0):
        break
    res+=1
print(f'LCM of the two numbers are {res}')


# and also LCM = (a*b)/gcd
