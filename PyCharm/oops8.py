
#-------------------------multiple inheritance--------------------------------#

class Employee:
    no_of_leaves = 8
    var = 8
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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f'name is {self.name}. Game is {self.game}.'

class CoolProgrammer(Player, Employee): #multiple inheritance, order of classes given matters
    #NOTE = IN MULTIPLE INHERITANCE, CONSTRUCTOR FOR COOLPROGRAMMER WILL BE TAKEN AS OF
    # SUPERIOR CLASS IN ORDER, PLAYER IN THIS CASE and not that of Employee
    # var =10
    languages = ['java', 'python']
    def printLanguage(self):
        print(self.languages)

harry = Employee('harry', 450, 'instructor')
rohan = Employee('rohan', 678, 'student')

shubham = Player("Shubham", ["Cricket"])

karan = CoolProgrammer("karan", ["CoolProgrammer"])
# det = karan.printDetails()
# print(det)
# karan.printLanguage()

print(karan.var)