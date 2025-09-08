 # Write a Python Program to get the count of prime number from the user's input list


def getSmallest(l:list)->int:
    small=l[0]
    for i in l:
        if small>i:
            small=i
    return small

print(getSmallest([1,2,3,4,5,6]))