# ---------------------Foods and calories------------------------

print("welcome to CodeWithHarry restaurant!")
#initialise a blank list
menu = []
#take the size of list from the user
num = int(input('Enter number of recipes you want:\n'))
print('Enter recipes you want:')

#take input from user
for i in range(num):
    item = input()
    menu.append(item)
print(menu)
# menu = [1,23,10,5,9]
'''
def reverse_inbuilt(ls):
    ls.reverse()
    return (ls)

def list_slice(lst):
    lst[::-1]
    return (lst)

def swap_elements(lis):
    n = len(lis)
    # ans = []
    for i in range(n):
        ans.append(lis[n-i-1])

    # print (ans)
    return  ans


# if  list_slice(menu) == swap_elements(menu):
print(list_slice(menu))

swap_elements(menu)
'''

# below code as per harry solution thats best:
reverse1 = menu[:] #NOTE - ithe nusta reverse1=menu kela asta ter original menu change hoto. Hence in order to make
# copy of the manu, make reverse1=menu[:]
reverse1.reverse()
print(f"my first reversed list of {menu} is {reverse1}")

reverse2 = menu[::-1]
print(f"my second reversed list of {menu} is {reverse2}")

reverse3 = menu[:]
for i in range(len(reverse3) //2): #using floordiv to get the int value
    #NOTE - len(reverse3) //2 ghetla cz nusta len(reverse3) aste teva list reverse houn parat original list milte :D
    # manun half length paryant reverse kraychi
    reverse3[i], reverse3[len(reverse3)-i -1] = reverse3[len(reverse3)-i-1], reverse3[i]
    print(f"the reversed list at i={i} is {reverse3} ")
print(f'my third reversed list of {menu} is {reverse3}')

# print(9//2)

if reverse1 == reverse3 and reverse3 == reverse2:
    print("all 3 methods give same result! congrats!")

