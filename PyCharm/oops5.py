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

    # @classmethod
    # def from_str(cls, string):
    #     params = string.split("-") #SPLIT IS RETURNING LIST TO PARAMS
    #     print(params)
    #     return  cls(params[0],params[1], params[2])

    # -----------alternative way of from_str classmethod as below using args and kwargs---------------------##
    @classmethod
    def from_str(cls,string):
        return cls(*string.split('-'))


harry = Employee('harry', 450, 'instructor') #NOTE = THESE ARGUMENTS ARE GOING TO INIT
rohan = Employee('rohan', 678, 'student')
karan = Employee.from_str('karan-922-student') #NOTE- DUE TO CLASSMETHOD AS ALTERNATIVE CONSTRUCTOR, NO NEED
#TO GIVE 3 DIFFERENT ARGUMENTS,

print(karan.salary)

#NOTE- THIS CAN BE USED WHEN DATA IS IN TEXT FILE IN ABOVE FORMAT FOR 50M USERS,
# SUCH ALTERNATIVE CONSTRUCTORS CAN BE USED, cant use split function multiple times as it will reduce
# efficiency of code
