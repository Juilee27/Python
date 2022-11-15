
import time
# def searcher():
#     # some 4 seconds time consuming task
#     book = "this is very long book which is taking 4 sec of time to read"
#     time.sleep(4)
#
#     while True:
#         text = (yield)  #NOTE- PYTHON KO KESE SMJEGA SEARCHER COROUTINE HE?
# # YE BRACES ME JO YIELD LIKHA HE USSE ..
#         if text in book:
#             print("your text is in the book")
#         else:
#             print('text is not in the book')
#
# search = searcher()
# print("search started")
# next(search) #next method code ko starting se chalata he
# print("next method run")
# search.send("har") #ye jo values dere he vo yield me jare he in while loop, code is not running from start
# input('press any key: \n')
# search.send("harry andf") #2nd time he patkan run zala karan while loop pasun execute zala
# #  and not from beginning
# input('press any key: \n')
# search.send("book")
# input('press any key: \n')
# search.send("book")
# input('press any key: \n')
# search.send("book")
#
# search.close() #we can close this coroutine and on closing , coroutine has released all resources
#
# search.send('ola')


# =================================EXERCISE=================================================#
# 15 letters in text file given
# design coroutine that will read this and find out and print aapka naam kisme he,
#  agar nai he toh print kre nai he
# naam input lo . coroutine banao and follow above design

def findtheName():
    with open("textforCoroutine.txt") as f:
        text = f.read()
        print('read file!')

    while 1:
        name = (yield) #coroutine
        if name in text:
            print('found your name!')
        else:
            print("ur name is missing.")


searchName = findtheName()
print("search started")
next(searchName) #run code from start
print("next method run")
searchName.send('jui')
input('press any key: \n')
searchName.send("lame") #lame pass kertoy not the user input
input('press any key: \n')
searchName.send("samba")
searchName.close()




