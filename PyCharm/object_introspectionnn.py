# what is object introspection?
# getting complete info about object is obj introsp.

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}_{lname}@gmail.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set. pl set it using setter. "
        else:
            return f"{self.fname}_{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print('setting now...........')
        names = string.split("@")[0]
        self.fname, self.lname = names.split(".")[0], names.split('.')[1]
        # self.fname = names.split(".")[0]
        # self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("skill", "F")
# print(skillf.email)

# print(type(skillf),'\n', id(skillf)) #every item has id
# print(dir(skillf))

import inspect


# print(inspect.getmembers(skillf))

def obj_introspec(obj):
    print(inspect.getdoc(obj))
    print(f" name of file in which object is defined is {inspect.getfile(obj)}")
    l = (inspect.classify_class_attrs(obj))
    for item in l:
        print(f'attributes are:\n{item}')


obj_introspec(Employee)
