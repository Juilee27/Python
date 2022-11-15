# file IO
# 'r' - open file for reading - default
# 'w' - open file for writing
# 'x' - creates file if it does not exist, if file is already existing no action is taken
# 'a' = append, add more content to end of file
# 't' = text mode - default
# 'b' = binary mode
# '+' = read and write

f = open('harry.txt', "rt") #this open function returns file pointer #rt is default mode
# content = f.read()
# content = f.read(3)
# print(content)

# content = f.read(3)
# content = f.read(34445)
# print('2', content)

# for line in f:
#     print(line, end='')

# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readlines())
f.close() #this is important practice, so that other programs can use it



