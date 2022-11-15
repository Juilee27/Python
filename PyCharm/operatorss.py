# operators in python
# arithmatic operators
# assignment operators
# comparison operators
# logical operators
# identity operators
# membership operators
# bitwise operators

# arithmatic operators
print('15//6 is: ', 15//6) #this is floor division operator- returns int
print('5 **3 is: ', 5**3) #this is 5 to the power 3- exponential
print('5 %5 is 5 mod 5 - gives remainder: ', 5%5)

#assignment operators
x=5
x %=7
print(x) # x= x%7

#identity operators - is and is not are identity operators
a= True
b= False
print(a is b)
print(a is not b)

#membership operators
list1 = [1,2,3,56,78]
print('\n', 25 in list1)
print(56 in list1)

#bitwise operators - useful in solving competitive problems as these are fastly implemented
# fast bcz machine understands boolean values quickly and computer likes to work with boolean logic
# quickly
# 0 = 00
# 1= 01
# 2= 10
# 3= 11

print(0|3)
print(1 & 2)