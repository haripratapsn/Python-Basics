# 12345
# 678910
# 1112131415
# 1617181920
# 2122232425

sides=int(input("Enter the length of the Square: "))
k=1
for i in range(1,sides+1):
    for j in range(1,sides+1):
        print(k, end=' ')
        k+=1
        
    print()

# sides=int(input("Enter the length of the Square: "))
# k=1
# for i in range(1,sides+1):
#     for j in range(1,sides+1):
#         print(f"{k:{2}}", end=' ')
#         k+=1
        
#     print()
