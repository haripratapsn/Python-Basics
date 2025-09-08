# Get Days of the month

def getDays(month):
    months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October","November","December"]
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print(f'{months[month-1]} has 31 days')
    elif month==2:
        print(f"{months[month-1]} has 28 days")
    else:
        print(f"{months[month-1]} has 30 days")
    
getDays(11)