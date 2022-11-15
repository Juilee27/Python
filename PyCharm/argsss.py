def func_name_print(a,b,c,d,e):
    print(a,b,c,d,e)
# func_name_print(1,3,55,66, 'deru')
#for multiple arguments this is not scalable

# def funargs(normal, *args): #we can pass any type of argument
# def funargs(normal, *argsrohan): #note- argsrohan is same as args, any name can be used
#     print(normal)
#     for item in argsrohan:
#     # print(type(args))
#         print(item)
#
# har = ['jian', 'jamai', 'jeka', 'jimin', 'jimmy','sumar','sumesh']
# normal = 'this is a normal'
# funargs(normal, *har)


# def funargs(*argsrohan, normal): #it is a convention to keep normal argument first, then *args
# # and *kwargs in this order
#     print(normal)
#     for item in argsrohan:
#         print(item)
#
# har = ['jian', 'jamai', 'jeka', 'jimin', 'jimmy','sumar','sumesh']
# normal = 'this is a normal'
# funargs(*har,normal)


def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f'this is key: ',key)

kw = {'1':'3','33':'44', 'ty':'ty', 'jam':'chana'}
har = ['jian', 'jamai', 'jeka', 'jimin', 'jimmy','sumar','sumesh']
normal = 'this is a normal'
# funargs(normal, *har) #kwargs parameter pass nai kia as args and kwargs are optional arguments
# even if we do not pass it it does not give error
funargs(normal, *har, **kw)

