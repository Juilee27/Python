# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Palindromify the List~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def isPallindrome(n):
    return str(n) == str(n)[::-1] #number pallindrome ahe ka te check kela


def nextPallindrome(n): #input no cha next pallindrome find krayla
    n = n + 1
    while isPallindrome(n) != True:
        n += 1
    return n


if __name__ == '__main__':
    # initialise blank list
    ans = []
    try:
        cases = int(input("Pls enter no of cases:\n"))
        ls = []

        # take user input and create list
        for i in range(cases):
            number = int(input("Enter number to find pallindrome:\n"))
            ls.append(number)

        # iterate above list and return list with desired output
        for k in ls:
            if k < 10:
                ans.append(k)
            else: #for no >10 ye next pallindrome rerurn krega
                ans.append(nextPallindrome(k))
        print(f"{ls} list is pallindromified to {ans}. ")


    except ValueError:
        print("PLease enter valid integer.")
