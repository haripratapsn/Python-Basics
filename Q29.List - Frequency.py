 # Write a Python Program to get the frequency of the element in the user's input list


# def getFrequency(l:list)->None:
#     freq=[]
#     visited=[]
#     for i in range(len(l)-1):
#         if l[i] not in visited:
#             count=0
#             for j in range(1,len(l)):
#                 if l[i]==l[j]:
#                     count+=1
#             freq.append((l[i],count))
#             visited.append(l[i])
#     for i,j in freq:
#         print(f"{i}->{j} times")

# getFrequency([1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5])


# Using Predefined Functions

from collections import Counter

def getFrequency(l:list)->list:
    freq=Counter(l) #Returns dict with key value pairs as the number and value as the count
    print(freq)
    for i,j in freq.items():
        print(f"{i} -> {j} times")

getFrequency([1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5])

