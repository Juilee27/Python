# -----------------Super() and overriding----------------------#

class A:
    classVar1 = 'I am a class var in class A'
    def __init__(self): #NOTE - AS THIS CONSTRUCTOR IS OVERRIDEN IN B, HENCE THIS ONE
        # IN CLASS a WILL NOT RUN
        self.var1 = "I am inside class A's constructor"
        self.classVar1 = 'instance var in class A' #self. - meaning this is instance var
        self.special = 'special'

class B(A):
    # classVar1 = 'I am a class var in class B'
    def __init__(self):
        super().__init__() #super - to aceess super class variables thru constructor
        self.var1 = "I am inside class B's constructor"
        self.classVar1 = 'instance var in class B'
        super().__init__()
        #NOTE - SUPER LA ITHE JER COMPLETELY COMMENT OUT KELA ANI CLASS B CHA
        #CONSTRUCTOR VER HOVER KELA TER WARNING MILTE, IT IS AS WE ARE NOT USING CODE REUSABILITY
        print(super().classVar1) #this will access super class var


a= A()
b = B()

# print(b.classVar1)
print(b.special,'\n', b.var1,'\n', b.classVar1)
