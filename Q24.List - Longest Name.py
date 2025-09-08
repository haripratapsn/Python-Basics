 # Write a Python Program to get names from the user and store it in a list then return the longest name


def getLongest(names:list)->str:
    longest=names[0]
    for name in names:
        if len(name)>len(longest):
            longest=name
    return longest

print(getLongest(["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah"]))




    