class Employee:
    no_of_leaves = 8
    def printDetails(self): #NOTE- SELF IS THAT OBJECT JISKI BAAT KI JA RAHI
# HE EXAMPLE RUNNING THIS METHOD ON HARRY, SELF IS HARRY
        return f'name is {self.name}. Salary is {self.salary}. Role is {self.role} '
    ##NOTE- EMPLOYEE KO ARGUMENTS DENE K LIYE INIT LGEGA

    def __init__(self, aname, asalary, arole): #NOTE - INIT IS CONSTRUCTOR
        self.name =  aname
        self.salary = asalary
        self.role = arole


harry = Employee('harry', 450, 'instructor') #NOTE = THESE ARGUMENTS ARE GOING TO INIT
rohan = Employee()

# harry.name = 'harry'
# harry.salary = 450
# harry.role = 'instructor'

# rohan.name = 'rohan'
# rohan.salary = 678
# rohan.role = 'student'

# print(harry.printDetails())


print(harry.role)