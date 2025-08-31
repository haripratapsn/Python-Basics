# AAAA
# bbbb
# CCCC
# DDDD


sides=int(input("Enter the length of the Square: "))

for i in range(1,sides+1):
    for j in range(1,sides+1):
        if i%2==0:
            print(chr(i+96),end='')
        else:
            print(chr(i+64),end='')

    print()

