# lists
numbers = [2, 3, 3, 3, 9, 13]
# numbers.sort()
# print(numbers.sort())
# numbers.reverse()
# print(numbers)

# print(numbers[57])

# print(numbers[:57])

# print(numbers[1:5])

print(numbers[::-1]) #like string this reverses the list

print(numbers[1:5:-3])  #use of negetive index is not recommended here in slcing bcz it
# does not work it gives empty list or string when index is greater than -1. it only works when [::-x]
#default values are mentioned due to some reason

print(max(numbers))

print(min(numbers))

# print(len(numbers))

# (numbers.append(34))
# print(numbers)

# (numbers.insert(4,79))
# numbers.remove(3)
# numbers.pop()  #this deletes last element
# print(numbers)
# numbers[3] = 103
# print(numbers)

tp = (1,2,3)
print(tp, type(tp))
tn = (2,)
print(tn, type(tn))

a=3
b=45
# temp = a
# a=b
# b=temp
# print('a=', a, 'b=', b)
#simple way to swap in python
a,b = b,a
print('a=', a, 'b=', b)


