# Write a Python Program to read the values from the user and store it in a list then return th sum of the list

def sumOfList(l:list)->int:
    sum=0
    for i in l:
        sum+=i
    return sum

print(sumOfList([1,2,5,3,4]))


