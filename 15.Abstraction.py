from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,color,name):
        self.color=color
        self.name=name
    @abstractmethod
    def draw(name):
        pass
    @abstractmethod
    def getArea(length,width):
        pass

class Person:
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def get_name(self):
        if self.__name is None:
            return "None"
        return self.__name

    def get_age(self):
        if self.__age is None:
            return "None"
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age