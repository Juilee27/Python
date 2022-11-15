# pattern printing
# inp =  int n
# boolean = true / false
#
# True n=4
# *
# **
# ***
# ****
# False n =4
# ****
# ***
# **
# *

# i = 1
try:
    n = int(input('enter no of rows: '))
    # var = int(input('enter true(1) / false(0): '))
    # var  = bool(var) #int ko bool me convert kerna he, string ko nai

    var = bool(int(input('enter true(1) / false(0): ')))

    if var == True:
#     # for i in range(1, n + 1):
#     #     print('*' * i)
#
# alternate way to do it
        for i in range(1, n + 1):
            for j in range(1, i+1):
                print('*',end=' ')
            print()




    if var == False:
    # for i in range(1, n + 1):
    #     print('*' * (n + 1 - i))

        for i in range(n,0,-1):
            print(i)
            for j in range(1, i+1):
                print('*',end=' ')
            print()

except Exception as e:
    print('invalid input!!')
