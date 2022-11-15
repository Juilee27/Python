d1 = {}
# print(d1, type(d1))
d2 = {'harry': 23, 'jui': 456, 'jolla': 'sola', 'ani': 'veda', 1: [7, 8, 90], (2,): 67,
      (129, 67): {1: 2, 'shuba': ['tola']}}
# print(d2, '\n', d2 [(129,67)][1] )
d2['sam'] = 45.93
d2[1] = 'jimin'
d2['45'] = 23
# print(d2)
del d2['jolla']
# print(d2)
# print(d2.copy())
#
# d3 = d2
# del d3['harry']
# print(d2)

# print(d2.get((2,)))

# d2.update({'Leena': 'toffee'})
# print(d2)

print(d2.keys() , d2.items())