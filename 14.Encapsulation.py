class Person():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def setName(self,name):
        self.__name=name

    def setAge(self,age):
        self.__age=age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    
    
    
        