# f= open('harry.txt', 'rt')
# print(f.readlines())

with open('harry.txt') as f:
    a= f.readlines()
    print(a)

j = open('harry.txt')
print(j.readline())

f.close()