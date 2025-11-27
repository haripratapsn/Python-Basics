 # Write a Python Program to get the reverse of the users's list


def getReverse(l:list)->list:
    reverse=l[::-1]
    return reverse

print(getReverse([1,2,3,4,5]))



# def getReverse(l:list)->list:
#     i=0
#     j=len(l)-1
#     while i<j:
#         l[i],l[j]=l[j],l[i]
#         i+=1
#         j-=1
#     return l

# print(getReverse([1,2,3,4,5]))


# def getReverse(l:list)->list:
#     reverse=[]
#     for i in range(len(l)-1,-1,-1):
#         reverse.append(l[i])
#     return reverse

# print(getReverse([1,2,3,4,5]))

