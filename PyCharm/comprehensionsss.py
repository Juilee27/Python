# COMPREHENSION GIVES GREAT SCALABILITY

# ls=[]
# for i in range (100):
#     if i%3==0:
#         ls.append(i)
# print(ls)
#above same list can be created in a simpler way using LIST COMPREHENSION as below (square braces)
# ls = [i for i in range(100) if i%3==0]
# print(ls)

# ------------DICTIONARY COMPREHENSION (curly braces)------------------------------
#note- this is best tool to reverse a dictionary
# dict1= {i:f"item{i}" for i in range (1000) if i%100==0}
# dict1= {i:f"item{i}" for i in range (5)}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict2)

# ------------SET COMPREHENSION (curly braces)------------------------------
# dresses = {dress for dress in ["dress1", 'dress2', 'dress1', "dress1", 'dress8']}
# print(dresses,'\n', type(dresses)) #set me unique values

# ------------Generator COMPREHENSION (round braces)------------------------------
# evens=(i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# #
# for item in evens:
#         print(item, end=" ")

# ----------small EXERCISE ------------------------------#
# user input  - vo list me kya kya item dalna chahta he and how many items
# for loop se list ko populate kro
# ask user - which type of comprehension do u want (any except generator comprehension)
# vo comprehension banva n  print it

# l1 = []
# num = int(input('Enter number of items you want to put: '))
# for i in range(num):
#         item = input('enter item: ')
#         l1.append(item)
# # print(l1)
# inp = input('which type of comprehension do u want to perform(list/set/dict): ')
# if inp == 'list':
#         ls= [item for item in l1]
#         print(ls)
# elif inp == 'dict':
#         dict1 = {i:l1[i] for i in range(num)}
#         print(dict1)
# elif inp == "set":
#         set1 = {item for item in l1}
#         print(f'{set1}\t {type(set1)}')


