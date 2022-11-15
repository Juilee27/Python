# example of caching - when we checking web page, computer will open browser, open YT, open playlist and
# save data on disk and open that page. on reloading, until it gets to know that page is updated,
# it will keep on showing page data it has earlier saved on disk. on reloading it just does not
# request data again blindly from internet
# same is the case with function caching
# we save function input and output value so that if someone runs func later, she will get cached values
# concluding we will not have to perform same task done by function again as already its previous values
# are cached and we can get it from there

import time
from functools import lru_cache  # functools is inbuilt module and lru_cache is decorator

#
# @lru_cache(maxsize=3) #NOTE-MAXSIZE 3 IS IT WILL SAVE LATEST 3 FUNC CALLS values
# def some_work(n):
#     # some task taking n seconds
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print('now running some work')
#     some_work(3) #ye run hoga tab delay ayega, ye value cache nai hua he as
#     # first time tun hua, run krke vo value cache krega
#     some_work(3) #this is cached
#     some_work(2) #this value is cached
# #some_work(3) - 2 vela run zala, first time run zala teva value cache keli hence next time
#     # same run hotana cached value retrieve keli python ne, similar implementation with other funcs
#     print('done, calling again')
#     some_work(3) #yahape caching se delay nai ayega
#     print('called again')

# result - on running this code, after printing now running some work, je 2 function
# calls ahet te delay cause karat nait due to func caching

# --------------small exercise--------------------------#
# make main func (main optional ahe)
# ask user how many values u wanna cache
# create func and lru cache use kro

#================= =========EXAMPLE 1=======================================#
num = int(input('Enter how many times u wanna cache values: '))

@lru_cache(maxsize=num)
def addwork(a, b, x):
    time.sleep(x) #this delay must be part of lru func
    return a + b

if __name__ == '__main__':
    print('enter the numbers u wanna addd:')
    a = int(input())
    b = int(input())
    print(addwork(a, b, 3))
    # time.sleep(3)
    print(addwork(a, b, 5))
    # time.sleep(3)
    print(addwork(a, b, 5))
    # time.sleep(3)
    print(addwork(a, b, 5))


#================= =========EXAMPLE 2=======================================#
n = int(input("Enter how many values you want to store"))
@lru_cache(maxsize=n)
def fibo(x):
    time.sleep(x)
    return x


if __name__ == '__main__':
    print("Calling 1st time ")
    fibo(3)
    print("Calling 2nd time ")

    fibo(5)
    print("Calling 3rd time ")

    fibo(5)
    print("Calling 4th time")
