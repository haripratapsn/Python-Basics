 # Q1.Write a Python Program to get only the common elements present in the lists given as user input

def getCommonEle(l1:list,l2:list)->list:
    common_ele=[]
    for i in l1:
        if i in l2 and i not in common_ele:
            common_ele.append(i)
    return common_ele

print(getCommonEle([1,2,3],[1,4,5,6]))
