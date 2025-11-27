# Write a program to perform Left shift on a list

def rightShift(l:list)->list:
    temp=l[-1]
    for i in range(len(l)-1,0,-1):
        l[i]=l[i-1]
    l[0]=temp
    return l

print(rightShift([1,2,3,4,5]))