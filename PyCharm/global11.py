# l=10 #Global - this is scope
# def func1(n):
#     # l=5 #local
#     m=7  #local
#
#     global l
#     l= l+45
#     ##note- first python looks for local var, if not found it searches for global var
#     # python has to give permission to change global var - to get this permission we
#     # will write scope inside function
#     print(l, m)
#     print(n,'I have printed')
#
# func1('Jila')
# print(l)
# try:
#     print(m)
# except Exception as e:
#     print('it is not global variable hence not getting its value')

x=98
def harry():
    x =56
    def rohan(): #ye rohan functio ne x namka global var banaya
        global x  #note = this global keyword will search for x var outside harry function ,
        # at very start
        x=88  #note = here we do not have global x var outside any functions, so above
        # global keyword created a x var and set it to x=88
    print('before calling rohan()',x)
    rohan()
    print('after calling rohan()',x)

harry()
print(x)