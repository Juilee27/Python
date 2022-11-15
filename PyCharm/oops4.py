class Employee:
    no_of_leaves = 8
    def printDetails(self): #NOTE- SELF IS THAT OBJECT JISKI BAAT KI JA RAHI
# HE EXAMPLE RUNNING THIS METHOD ON HARRY object, SELF IS HARRY
        return f'name is {self.name}. Salary is {self.salary}. Role is {self.role} '
    ##NOTE- EMPLOYEE class KO ARGUMENTS DENE K LIYE INIT LGEGA

    def __init__(self, aname, asalary, arole): #NOTE - INIT IS CONSTRUCTOR
        self.name =  aname
        self.salary = asalary
        self.role = arole

    @classmethod #NOTE- USE CLASSMETHOD decorator TO ELIMINATE SELF ARGUMENT, to only play with CLASS
    #CLASSMETHOD WILL ONLY BE ABLE TO ACCESS CLASS VARIABLE, WE CAN ACCESS IT USING CLASS
    # AS WELL AS INSTANCE
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


harry = Employee('harry', 450, 'instructor') #NOTE = THESE ARGUMENTS ARE GOING TO INIT
rohan = Employee('rohan', 678, 'student')

# rohan.change_leaves(45)
Employee.change_leaves(5)

print(Employee.no_of_leaves)
print(harry.no_of_leaves)