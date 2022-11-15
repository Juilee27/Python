# for loop - tut16 quiz

list1 = ['97.hh', """57676767hjhkh""", 89, 4, 5, 6, 7, 9.67, 6]
for item in list1:
    if str(item).isnumeric() and item >6:  #str of item bcz isnumeric fn checks string
            print(item)
    else:
        print('item is not an integer')
