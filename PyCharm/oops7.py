#ABSTRACTION KO ACHIEVE KRNE K LIYE ENCAPSULATION KERNA PDTA HE

#--------------inheritance===========================#

class Employee:
    no_of_leaves = 8
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

class Programmer(Employee): #single inheritance
    def __init__(self,aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printProg(self):
        return f'name is {self.name}. Salary is {self.salary}. Role is {self.role}. ' \
               f'languages are {self.languages}'

harry = Employee('harry', 450, 'instructor')
rohan = Employee('rohan', 678, 'student')

shubham = Programmer('shubham', 155, 'programmer', ["python"])
# karan = Programmer.from_str('karan-922-student')
karan = Programmer('karan',922, 'student', ['java', 'cpp'])

print(karan.printProg())
