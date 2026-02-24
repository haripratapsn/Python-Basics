class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def isAdult(age):
        return (age>18)
    
    def print_details(self):
        print(self.name)
        print(self.age)
        print(Person.isAdult(self.age))

object_var=Person("Spark",22)
object_var.print_details()
object_var.isAdult(object_var.age)


