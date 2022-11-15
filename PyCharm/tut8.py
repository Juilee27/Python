myStr = 'harry is a good boy'
gem = "4j4j4j4j4j4j4"
print(myStr[0:len(myStr)])

print(myStr[6])

# print(myStr[67])
# print(myStr[0:78])

# print(myStr[0::1])  # this is similar to print(myStr[:len(myStr):])

# print(myStr[0::12])

# print(myStr[0::1245])  # it will resolve to extend possible for it

# print(myStr[::-1])  # this reverses the string, so this minus skipping first reverses the string then slicing hoga

print( gem.isalnum())
print(myStr.isalpha())
print(myStr.endswith('boy'))
print(myStr.count('0'))
print(myStr.capitalize())
print(myStr.find('is'))
print(myStr.upper())
print(myStr.lower())
print(myStr.replace('is', "har"))