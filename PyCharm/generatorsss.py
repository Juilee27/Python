"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - performing this is iteration


"""
def gen(n): #trying to make our own generator
    for i in range (n):
        yield i #generator help to save ram, they generate values on the fly,
        # yield is different than return and print
        #generator is generating it but not storing in ram, we can use it when required
        #generator ese iterator hote jinko can be used only  once

g= gen(3)
# print(g)
# g.__next__()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())



# for i in range (78): #for loop is designed in such a way that when stopitration occurs
# loop stops there without error
#     print(i)

h='harry' #string is ITERABLE hence it has __iter__ method
# print(iter(h))

ier= iter(h)  #note- iterrate kro fir generator chal jaega
print(ier.__next__())
print(ier.__next__())

# for c in h:
#     print(c)