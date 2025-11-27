 # Write a Python Program to get the highest frequency of the element in the user's input list

from collections import Counter
def getHigestOccurredElement(l:list)->int:
    freq=Counter(l)
    high_value=0
    high_freq=0
    for i,j in freq.items():
        if j>high_freq:
            high_freq=j
            high_value=i
    return f"{high_value}->{high_freq} Times"

print(getHigestOccurredElement([1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]))   