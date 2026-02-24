class Employee:
    company_name="gfg"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def setCompanyName(cls,cName):
        cls.company_name=cName
        print(cls)
        print(cls.company_name)
    
    def print_all(self):
        print(self)
        print(self.company_name)

object_var=Employee("Hari",22)
object_var.print_all()
object_var.setCompanyName("pratap")

print(Employee)