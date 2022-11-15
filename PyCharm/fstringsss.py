#f strings
'''f in fsting has full form fast literally'''
import  math
me = 'harry'
a1=3
#
# a= 'this is %s %s'%(me,a1)  #this string is not readable and managable
# print(a)

# a= 'this is {} {}' #by default this takes index 0,1...me has zero index and a1 has index 1
# a= 'this is {1} {0}'
# b= a.format(me,a1)
# print(b)

a= f"this is {me} {a1} {4*65} {math.cos(56)}"
print(a)


