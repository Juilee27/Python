
#---------operator overloading and dunder methods----------------
#what is a dunder method? - __ se start hone vale and __ se end hone vale methods
#for operator overloading, checkout page - mapping operators to functions python

class Employee:
    no_of_leaves = 8

    def printDetails(self):
        return f'name is {self.name}. Salary is {self.salary}. Role is {self.role} '

    # -----------init is special dunder init method-----------------
    def __init__(self, aname, asalary, arole): #NOTE - this is special dunder method
        self.name =  aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

#-----------dunder add method-----------------
#NOTE - WHENEVER ADDING 2 OBJECTS OF SOME CLASSES, in backend python is running dunder add method and
    #this method is helping us to do operator overloading
    #BUT NOTE EVERY DUNDER METHOD DOES NOT NECESSARILY PERFORM OPERATOR OVERLOADING

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other): #this method is overloading slash operator
        return  self.salary / other.salary

    def __repr__(self):
        return self.printDetails(), f"this is it"

    def __str__(self): #object kya he ye dekhne ke liye str use krte
        return f'name is {self.name}. Salary is {self.salary}. Role is {self.role} '

    def __ge__(self, other):
        return  self.salary >= other.salary

emp1 = Employee('harry', 5600, 'banker') #keep cursor on line and place ctrl D to replicate it
emp2 = Employee('jinna', 6700, 'cleaner')
# print(emp1 + emp2)

# print(emp1/emp2)
print(emp1) #emp1 str ko print kerna pehle prefer krta he

print(emp1.__repr__()) #repr ko call kia tohi vo run hoga otherwise str prefer hoga
# and agar str nai he toh any case me vo repr call krta even if we have written print(str(emp1))

print(emp1 >= emp2)