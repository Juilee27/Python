# ~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~Rohan Das is a Fraud~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random

'''def rohanMultiplication(num):
    ls = []
    i = 1
    while i != 7: #6 paryant vales multiply kela
        op = num * i
        ls.append(op) 
        i += 1
    op = random.randint(5, 89) #7 la hi random value ali
    ls.append(op)
    for j in range(8, 11):
        op = num * j
        ls.append(op) #8-10 hya values alya
    print(ls)
    return ls

def isCorrect(number):
    wrong = rohanMultiplication(number)  #this is giving wrong table
    correct = []
    for k in range(1,11):
        result = number * k
        correct.append(result)   #this is giving correct table
    # print(correct)
    for b in range(1,len(correct)):
        if correct[b] != wrong[b]: #2 lists compare kelya
            print(f"Rohan's table is wrong at index {b}. The incorrect value is {wrong[b]}")

if __name__ == '__main__':
    isCorrect(9)
'''


# -----------------following is the Harry's solution -------------------------
def rohanMultiplication(num):
    wrong = random.randint(0, 9)  # hyane index wrong gheun kela and me value gheun kela
    table = [num * i for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(1, 10)  # table cha wrong index value madhe thodi value add keli
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number: #table list ahe manun i-1 index,
            return i-1  #index jithe value wrong ahe te return kerto

    return None  #agar kuch galat nai mila toh return None

if __name__ == '__main__':
    inp = int(input('enter some number:\n'))
    table = rohanMultiplication(inp)
    print(table)
    incor = isCorrect(table, inp)
    print(f"incorrect value is found at index {incor}")
