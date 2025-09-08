# Biggest number of 3 numbers

# def isBiggest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
    
# print(isBiggest(1,2,3))




def isBiggest(a:int,b:int,c:int)->int:
    big=a
    if b>big:
        big=b
    if c>big:
        big=c
    return big

print(isBiggest(1,2,3))