# create a dictionary and take input from the user and return meaning of the word from the dictionary

d1 = {'set': "non repetitive values",
      'tuple': "non mutable",
      "string": 'zero index',
      'list': "it is also mutable datatype",
      'dictionary': 'dict is also indexed'}

a = input("please enter your word : ")
# if a in d1:
#     print(d1.get(a))
#
# else:
#     print('not found')

print(d1[a])
