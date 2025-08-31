import copy
s=[10,20,30,[50,60,70]]
d=copy.deepcopy(s)
print(s)
print(d)
print(id(s))
print(id(d))
print(id(s[3]))
print(id(d[3]))
s[2]=90
print(s)
print(d)
d[3][1]=100
print(d)
print(s)
