 # Write a Python Program to remove the duplicate element from the user's input list without using set

def removeDuplicate(l:list)->list:
    unique=[]
    for i in l:
        if i not in unique:
            unique.append(i)
    return unique

print(removeDuplicate([1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]))
    