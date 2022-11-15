# a= input("what is your name\n")
# b= input("how much do u earn?")
#
# if int(b)==0:
#     raise ZeroDivisionError("b is zero so stopping the program")
#
# if a.isnumeric():
#     # pass
#     raise Exception("numbers are not allowed")
#
# print(f"hello {a}")
#1000 lines of code taking one hour





c = input("enter ur name\n")
c= c.lower()
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked He is not allowed")

    print("exception handled")