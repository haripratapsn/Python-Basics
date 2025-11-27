# Greatest Common Divisor
# Euclanodian Algorithm is the best way to find GCD - Greatest common Divisor but this program is not based on this algorith

a=int(input("Enter a Number: "))
b=int(input("Enter b Number: "))
small=min(a,b)

for i in range(1,small+1):
    if (a%i==0 and b%i==0):
        gcd=i
print(f"Gcd is {gcd}")