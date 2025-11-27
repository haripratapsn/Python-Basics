 # Write a Python Program to get the frequency of the element in the user's input list using dictionary

def getFrequency(l:list)->None:
    freq={}
    for i in l:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    #Unpacking 
    for i in freq:
        print(f"{i}->{freq[i]} times")

getFrequency([1,2,1,2,3])