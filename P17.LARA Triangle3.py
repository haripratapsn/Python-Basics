#     1 
#     0 0 
#     1 1 1 
#     0 0 0 0 


n=int(input("Enter n value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i%2,end="")
    print()

