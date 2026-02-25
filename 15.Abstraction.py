from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,color,name):
        self.color=color
        self.name=name
    @abstractmethod
    def draw(name):
        return
    @abstractmethod
    def getArea(length,width):
        return
