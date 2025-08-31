s=[10,20,[50,20,30]]
d=s.copy()
print(s)
print(d)
s[0]=70
print(s)#source values are only changed.
print(d)
s[2][1]=100 #In nested list the it only copy's the value space conted of the source
print(s)
print(d)




