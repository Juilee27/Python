class Employee:
    @staticmethod #decorator #this function is only want to use for employee class hence created inside class
    def printgood(string):
        print('this is good' +string)

karan = Employee()
karan.printgood(' code')

Employee.printgood(''' practice''')