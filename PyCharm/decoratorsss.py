# def func1():
#     print('subscribe now')
#
# func2 = func1
#
# del func1 #deleted func1
# func2()

# def funcret(num):
#     if num==0:
#         return print, sum #it is returning print function here
#     if num==1:
#         return int #it is returning int function here
# a= funcret(0)
# print(a)

# def executor(func):  # we can put funtion as argument inside function
#     func('this')
#
#
# executor(print)
# # executor(sum)

##---------------DECORATORS-------------------------##
##--USE OF DECORATORS: WHEN WE WANT TO PERFORM SAME TASK WITH 10 FUNCTIONS SAY
# THAT TIME WE MAKE ITS DECORATOR CREATING A BLUEPRINT AND @dec1 KEYWORD SE USE KERTI RHEGI

def dec1(func1):
    def nowexec():
        print('executing now')
        func1()
        print('executed')

    return nowexec


@dec1
def who_is_harry():
    print('harry is a good boy')


# who_is_harry = dec1(who_is_harry) #this line can also be done writing dec1 above who_is_harry()

who_is_harry()
