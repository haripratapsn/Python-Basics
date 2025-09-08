 # Write a Python Program to get the frequency of the specified element in the user's input

def getFrequency(l:list,ele:int)->None:
    freq={}
    for i in l:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    #Unpacking 
    for i in freq:
        if i==ele:
            print(f"{i}->{freq[i]} times")
            break

getFrequency([1,2,1,2,3],2)