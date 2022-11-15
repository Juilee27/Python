list1 = [5, 7, 3]
if 5 in list1:
    print('5 is in the list')
if 15 not in list1:  # not and in are 2 different keywords
    print('yes it is not in the list')

age = int(input('enter your age: '))
if age in range(1, 100):
    if age == 18:
        print('we will decide')
    elif age < 18:
        print('cannot get licence')
    elif age > 18:
        print('can get dL')
else:
    print('age OOR')
