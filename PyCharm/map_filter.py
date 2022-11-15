#----------MAP FUNCTION-----------------#

# numbers = ['3', '34', '64']

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     numbers[i]  =   numbers[i] +1
#     print(numbers[i])

# print(map(int,numbers))

# numbers = list(map(int, numbers)) ##NOTE- Map FUNC RAN INT FUNC ON ALL ITEMS OF NUMBERS
# numbers[2] = numbers[2] +1
# print(numbers[2])

# def sq(a):
#     return a*a
# num = [23,4,5,67,78,9,67,8.9]
# square = list(map(sq,num))
# print(square)

# num = [23,4,5,67,78,9,67,8.9]
# square = list(map(lambda x: x*x,num))
# print(square)

# def square (a):
#     return a*a
#
# def cube(a):
#     return  a*a*a
#
# func = [square, cube]
# num = [23,4,5,67,78,9,67,8.9]
# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)

#----------FILTER FUNCTION-----------------#

# list_1 = [1,2,3,4,5,6,7,8,9,90]
#
# def is_greater_5(num):
#     return  num>5 #this will return true/false
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

#----------REDUCE FUNCTION-----------------#
from functools import reduce
ls1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, ls1)
print(num)





