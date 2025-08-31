# AAAA
# BBBB
# CCCC
# DDDD

sides=int(input("Enter the length of the Square: "))

for i in range(1,sides+1):
    for j in range(1,sides+1):
        print(chr(64+i), end=' ')
    print()

