
# # lambda / anonymous function
# def sum(a,b):
#     return a+b
#
# minus = lambda  x,y: x-y
# #this is similar to below function
# # def minus(x,y):
# #     return  x-y#
# print(minus(56,5))

# def a_first(a):
#     return a[1]
#
a=[[1,78],[5,-9],[8,23]]
# a.sort(key= a_first)  #note = key is argument which takes function as input
# print(a)
#we will try above same function with lambda
a.sort(key=lambda x:x[1])
print(a)
