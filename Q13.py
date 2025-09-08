# Get smallest number of 3

# def getSmallest(a,b,c):
#     if a<b and a<c:
#         return a
#     elif b<c:
#         return b
#     else:
#         return c
    
# print(getSmallest(2,1,3))

def getSmallest(a,b,c):
    small=a
    if b<small:
        small=b
    if c<small:
        small=c
    return small

print(getSmallest(2,1,3))