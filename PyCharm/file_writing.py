f = open('harry.txt', "w")
# f = open('harry.txt',"a")
# f.write('harry bhai bahut ache he \n')
a = f.write('harry bhai bahut ache he \n')
# print(a)

# handle read and write both
f = open('harry.txt', "r+")
print(f.read())
f.write('thank you')

# f=open('harry.txt')
print(f.read())

f.close()

