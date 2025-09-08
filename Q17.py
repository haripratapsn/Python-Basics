# Leap Year

# def isLeafYear(year):
#     if year%4==0 and year%100!=0:
#         print(f"{year} is a leaf year")
#     elif year%400==0:
#         print(f"{year} is a leaf year")
#     else:
#         print(f"{year} is not a leap year")

# isLeafYear(2000)

def isLeafYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"{year} is a leaf year")
    else:
        print(f"{year} is not a leap year")

isLeafYear(2004)