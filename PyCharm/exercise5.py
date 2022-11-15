# health management system
# import datetime

# 3 clients - harry,rohan , hamad
# create 6 files - 3 for their food log, 3 for their exercise
# write a function that when executed takes as input client name , a name of client
# associated with its number can also be taken for eg 1 for rohan
# use below fn:
# def getDate():
#     # import datetime
#     # return datetime.datetime.now()
#
# use above fn to include time - eg - [timestamp] chicken curry

# one more fn to ask program to log/ retrieve exercise/ food for any clinet
# solution -- NOTE: this code can also be written using list / dictionary


import datetime


def getDate():
    return datetime.datetime.now()  # this function is given by harry


def clientName(A):
    if A == 1:
        print(' --Data for Harry--')
    elif A == 2:
        print('-- Data for Rohan--')
    elif A == 3:
        print('--Data for Hamad--')


def data(A, B, C):
    if B == 'log' and C=='food' :
        if A == 1 :
            f = open('Harry_Food.txt', 'a')
            no_of_items = int(input('enter no of food items to enter: '))
            for i in range(no_of_items):
                harry_food = input('enter food item eaten today: ')
                f.write('['+ str(getDate())+ ']'+ ' ' + harry_food + '\n')


        elif  A == 2 :
            f = open('Rohan_Food.txt', 'a')
            no_of_items = int(input('enter no of food items to enter: '))
            for i in range(no_of_items):
                rohan_food = input('enter food item eaten today: ')
                f.write('['+ str(getDate())+ ']'+ ' ' + rohan_food + '\n')

        elif A == 3 :
            f = open('Hamad_Food.txt', 'a')
            no_of_items = int(input('enter no of food items to enter: '))
            for i in range(no_of_items):
                Hamad_food = input('enter food item eaten today: ')
                f.write('['+ str(getDate())+ ']'+ ' ' + Hamad_food + '\n')

    if B == 'log' and C=='exercise' :
        if A == 1 :
            f = open('Harry_exercise.txt', 'a')
            no_of_items = int(input('enter types of exercises to enter: '))
            for i in range(no_of_items):
                harry_exercise = input('enter exercise performed today: ')
                f.write('['+ str(getDate())+ ']'+ ' ' + harry_exercise + '\n')

        elif A == 2:
            f = open('Rohan_exercise.txt', 'a')
            no_of_items = int(input('enter types of exercises to enter: '))
            for i in range(no_of_items):
                rohan_exercise = input('enter exercise performed today: ')
                f.write('['+ str(getDate())+ ']'+ ' ' + rohan_exercise + '\n')

        elif A == 3:
            f = open('Hamad_exercise.txt', 'a')
            no_of_items = int(input('enter types of exercises to enter: '))
            for i in range(no_of_items):
                hamad_exercise = input('enter exercise performed today: ')
                f.write('['+ str(getDate())+ ']'+ ' ' + hamad_exercise + '\n')
        #
    if B == 'retrieve' and C == 'food':
        if A==1:
            f = open('Harry_Food.txt')
            print(f.read())

        elif A==2:
            f = open('Rohan_Food.txt')
            print(f.read())

        elif A==3:
            f = open('Hamad_Food.txt')
            print(f.read())

    if B == 'retrieve' and C == 'exercise':
        if A == 1:
            f = open('Harry_exercise.txt')
            print(f.read())

        elif A == 2:
            f = open('Rohan_exercise.txt')
            print(f.read())

        elif A == 3:
            f = open('Hamad_exercise.txt')
            print(f.read())



    f.close()


print("''''''''''''''Health management system''''''''''''''''''''''''''")
inp = input('press q to quit')

while inp != 'q':
    a = int(input('enter 1 for Harry\n '
              'enter 2 for Rohan \n'
              'enter 3 for Hamad\n '))
    clientName(a)

    b = input('Do you want to log/ retrieve data?: ')
    b = b.lower()

    c= input('is this data related to food / exercise?: ')
    c=c.lower()

    data(a, b, c)
