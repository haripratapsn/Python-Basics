# Get Month

def getMonth(month):
    months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October","November","December"]
    if 1<=month<=len(months):
        print(months[month-1])
    else:
        print("Invalid month number")

getMonth(11)