 # Write a Python Program to get the difference b/w biggest and smallest number in the user's input list


def diff(l:list)->int:
    return max(l) - min(l)

print(diff([1,2,3,4,5]))



# def getBiggiest(l:list)->int:
#     big=l[0]
#     for i in l:
#         if big<i:
#             big=i
#     return big

# def getSmallest(l:list)->int:
#     small=l[0]
#     for i in l:
#         if small>i:
#             small=i
#     return small

# def diff(l:list)->int:
#     return getBiggiest(l) - getSmallest(l)

# print(diff([1,2,3,4,5]))







    



