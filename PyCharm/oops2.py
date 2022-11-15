class Employee:
    no_of_leaves = 8
    pass
harry = Employee()
rohan = Employee()

harry.name = 'harry'
harry.salary = 450
harry.role = 'instructor'

rohan.name = 'rohan'
rohan.salary = 678
rohan.role = 'student'
# print(harry.salary)
# print(rohan.no_of_leaves,'\t', Employee.no_of_leaves) #NOTE - CLASS VARIABLES CAN BE
# ACCESSED VIA INSTANCE AND CLASS BOTH
Employee.no_of_leaves = 94 ##NOTE - CLASS VARIABLES CAN BE CHANGED ONLY BY USING CLASS, NOT BY OBJECT
print(Employee.no_of_leaves)
print(Employee.__dict__)
print(harry.__dict__)
harry.no_of_leaves = 5
print(harry.__dict__)
print(Employee.no_of_leaves) ##NOTE - WE TRIED CHANGING CLASS VAR USING INSTACE, BUT IT DID NOT CHANGE.
# ONLY INSTACE VAR GOT UPDATED
