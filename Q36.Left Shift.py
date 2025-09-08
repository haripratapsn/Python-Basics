# Write a program to perform Left shift on a list

# def leftShift(l:list)->list:
#     if len(l)==0:
#         return l
#     temp=l[0]
#     for i in range(1,len(l)):
#         l[i-1]=l[i]
#     l[-1]=temp
#     return l

# print(leftShift([1,2,3,4,5]))


def leftShift(l:list)->list:
    if len(l)==0:
        return l
    temp=l[0]
    for i in range(0,len(l)-1):
        l[i]=l[i+1]
    l[-1]=temp
    return l

print(leftShift(leftShift(leftShift([1,2,3,4,5]))))
