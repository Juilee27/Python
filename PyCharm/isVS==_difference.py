
# equality operator: == value eqality meaning 2 objects have the same value
# identity operator: is = reference equality meaning 2 references refer to same object
a = [6,4,"34"]
b = [6,4,"34"]
# a=b
print(b == a) #value is same hence True
print(b is a) # a and b pointing to 2 different objects at 2 different locations hence False