class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}_{lname}@gmail.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname== None or self.lname== None:
            return "email is not set. pl set it using setter. "
        else:
            return f"{self.fname}_{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print('setting now...........')
        names = string.split("@")[0]
        self.fname, self.lname = names.split(".")[0], names.split('.')[1]
        # self.fname = names.split(".")[0]
        # self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

hind = Employee("hindu", 'pande')
nik = Employee('nikhil','kamat')

print(hind.email)

hind.fname = "US"
print(hind.email) #jab object banaya tab constructor ko hindu fname pass kia, hence email did not change
#this problem is solved by setter. As per concept of encapsulation, i do not want to show this implementation
# to user. so we will use property decorator

hind.email= "abc.support@yahoo.com"
print(hind.fname, hind.lname, hind.email)

del hind.email
print(hind.fname, hind.lname, hind.email)

hind.email = "jimin.larry@yahoo.com"
print(hind.email)
