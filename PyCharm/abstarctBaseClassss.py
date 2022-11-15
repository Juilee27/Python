# ---------Abstarct base class and @abstractmethod----------------------

# from abc import ABCMeta, abstractmethod #for python versions above 3.4, following simpler syntax can also be used:
from abc import ABC, abstractmethod

# class Shape(metaclass= ABCMeta): #Shape is abstract class here , and this syntax for above 3.4 versions can be:
class Shape(ABC):
    @abstractmethod #meaning all classes must define this method
    def printArea(self):
        return  0

class Rectangle(Shape):
    type = 'rectangle'
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printArea(self): #basically we are forcing to run printArea method in this class
        return  self.length * self.breadth

rect1 = Rectangle()
print(rect1.printArea())

# tryObj = Shape() #NOTE- CANNOT CREATE OBJECT, CANNOT INSTANTTIATE OF ABSTRACT BASE CLASS