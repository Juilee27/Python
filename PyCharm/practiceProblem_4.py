# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ The Next Pallindrome~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
##Ha maza code ahe , this works great! pan harry cha pan try kruya! Y not!
def pallindrome(num):
    while 1:
        strin = str(num)
        #initialise empty string and list
        a = ''
        ls = []
        for i in range(len(strin)):
            # a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i] #NOTE = string is immutable, assignment does not work in str
            ls.append(strin[len(strin) - i - 1])
        #a string la populate kela with list contents
        q = a.join(ls)
        # print(q)
        #pallindrome ahe ka check krayla ani nasel ter next pallindrome number find krayla
        if q != strin:
            num+=1
            continue
        #jer single digit int asto ter to pallindrome show krat hota that is wrong hence we checked in this way
        elif len(q) ==1:
            while num!=10:
                num+=1
            # continue- ithe continue chi garaj nai
        else:
            print(f"next pallindrome is {int(q)}")
            break


if __name__ == '__main__':
    try:
        cases = int(input("Enter number of test cases:\n"))
        for i in range(cases):
            number = int(input("Enter integer to find next corresponding pallindrome:\n"))
            pallindrome(number)

    except ValueError:
        print("Please enter valid integer.")
        exit()
'''


# Harry cha code:

def isPallindrome(num):
    return str(num) == str(num)[::-1] #number pallindrome ahe ka te check kela

#aim is to find next pallindrome number, harry ne single digit cha case chi take care nai leliye
def nextPallindrome(num):
    if num >= 10:
        num = num + 1
        while not isPallindrome(num):
            num += 1
        return num
    else:
        while num!=10:
            num = num+1
        while not isPallindrome(num):
            num += 1
        return num

if __name__ == '__main__':
    try:
        cases = int(input("Pls enter no of cases:\n"))
        for i in range(cases):
            number = int(input("Enter number to find pallindrome:\n"))
            print(f"next pallindrome to is {nextPallindrome(number)}")
    except ValueError:
        print("PLease enter valid integer.")
