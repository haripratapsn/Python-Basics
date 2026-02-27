class Employee():
    company_name="Hari"
    def __init__(self,name):
        self.name=name
    def fun(self,n):
        self.name=n

e=Employee(1001)
print(e.company_name)
print(e.name)
e.fun("Sandeep")
print(e.name)
e.designation="CEO" #Explicit creation of instance variable
print(e.designation)
Employee.officeLoc="Bengalru" #Explicit creation of class level variable
print(e.officeLoc)


class Parent(Employee):
    def __init__(self,name,designation):
        super().__init__(name)
        super().designation
