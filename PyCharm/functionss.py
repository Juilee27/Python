# a=8
# b=5
# c = sum([a,b]) #or sum((a,b)) - iterable list naito tuple input chaiye
# print(c)

def function1(a, b):
    print('hello you are in function 1', a + b)


# print(function1())
# function1(5,8)
# function1()
# function1()

def function2(a, b):
    '''this is a function which will calculate average of 2 numbers'''  # this is docstring,
    # 1st line that is written in function
    avg = (a + b) / 2
    # print(avg)
    return avg


# v = function2(2,3)
# print(v)

# function2(4,6)
print(function2.__doc__)
