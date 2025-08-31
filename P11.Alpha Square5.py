# ABCD
# EFGH
# IJKL
# MNOP


sides=int(input("Enter the length of the Square: "))
k=1
for i in range(1,sides+1):
    for j in range(1,sides+1):
        print(chr(64+k), end=' ')
        k+=1
    print()

