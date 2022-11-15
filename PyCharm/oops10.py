# Public- ANY CLASS , ANY PART OF CODE CAN ACCESS VAR
# private - ONLY THAT CLASS WHERE IT IS DEFINED CAN ACCESS VAR
# protected -only CLASS AND ITS SUBCLASSES CAN ACCESS VAR

class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 90 #NOTE- VAR NAME STARTED WITH UNDERSCRORE AS WANT TO CREATE PROTECTED VAR
    __private = 4 #NOTE- VAR NAME STARTED WITH double UNDERSCRORE AS WANT TO CREATE private VAR
    def printDetails(self):
        return f'name is {self.name}. Salary is {self.salary}. Role is {self.role} '

    def __init__(self, aname, asalary, arole): #NOTE - INIT IS CONSTRUCTOR
        self.name =  aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split('-'))

emp = Employee("Jin", 5000, "TL")
print(emp._protec)
# print(emp.__private) #NOTE= WON'T BE ABLE TO ACEESS BY JUST VAR NAME, AS PYTHON HAS DONE NAME MANGLING,
# meaning python has made its name complex
#---------to access this private var------------------------#
print(emp._Employee__private) #note = PYTHON HAS SAVED IT AS _Employee__private
