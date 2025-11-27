 # Write a Python Program to get the count of prime number from the user's input list


def isPrime(n:int)->bool:
    if n==0 or n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        else:
            return True
        
def countPrime(plist:list)->int:
    count=0
    for number in plist:
        if isPrime(number):
            count+=1
    return count

print(countPrime([2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20]))

