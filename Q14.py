# Finding Middle Value so using maths aproach middle_value=(sum of all the number)-(highest value + lowest value)


def getBiggest(a:int,b:int,c:int)->int:
    big=a
    if b>big:
        big=b
    if c>big:
        big=c
    return big


def getSmallest(a,b,c):
    small=a
    if b<small:
        small=b
    if c<small:
        small=c
    return small


def getMiddle(a,b,c):
    h=getBiggest(a,b,c)
    l=getSmallest(a,b,c)
    middle_value=(a+b+c)-(h+l)

    return middle_value

print(getMiddle(1,2,3))

# Using Sorted()

def Display(a,b,c):
    s=sorted((a,b,c))
    m=len(s)//2
    print(s[m])

Display(1,2,3)