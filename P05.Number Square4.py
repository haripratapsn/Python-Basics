# 1111
# 0000
# 1111
# 0000

sides=int(input("Enter the length of the Square: "))

for i in range(1,sides+1):
    for j in range(1,sides+1):
        print(i%2, end=' ')
    print()
