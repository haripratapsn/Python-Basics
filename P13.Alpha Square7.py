# AAAA
# bbbb
# CCCC
# DDDD



sides=int(input("Enter the length of the Square: "))
k=0
for i in range(1,sides+1):
    for j in range(1,sides+1):
        print(chr(k%26+65),end='')
        k+=1
    print()


# sides=int(input("Enter the length of the Square: "))
# k=65
# for i in range(1,sides+1):
#     for j in range(1,sides+1):
#         print(chr(k),end='')
#         k+=1
#         if k==91: #if the ord is exceds after 91 then the ord of 92 is a special character so we reassign it to 65
#             k=65
#     print()
