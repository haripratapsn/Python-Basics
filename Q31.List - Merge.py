 # Q1.Write a Python Program to merge two list give as a user input without using plus operator


def merge(l1:list,l2:list)->list:
    for i in l2:
        l1.append(i)
    return l1

print(merge([1,2,3],[4,5,6]))




# Q2.In Zig Zag Manner

# def merge(l1:list,l2:list)->list:
#     l=[]
#     i=0
#     j=0
#     while i<len(l1) and j<len(l2):
#         l.append(l1[i])
#         l.append(l2[j])
#         i+=1
#         j+=1
#     while i<len(l1):
#         l.append(l1[i])
#         i+=1
#     while j<len(l1):
#         l.append(l2[j])
#         j+=1
#     return l

# print(merge([1,2,3],[4,5,6]))



# Q3.where the final list is sorted

# def merge(l1:list,l2:list)->list:
#     sorted_list=[]
#     i=0
#     j=0
#     while i<len(l1) and j<len(l2):
#         if l1[i]<l2[j]:
#             sorted_list.append(l1[i])
#             i+=1
#         else:
#             sorted_list.append(l2[j])
#             j+=1
#     while i<len(l1):
#         sorted_list.append(l1[i])
#         i+=1
#     while j<len(l2):
#         sorted_list.append(l2[j])
#         j+=1

#     return sorted_list
# print(merge([1,2,3],[4,5,6]))