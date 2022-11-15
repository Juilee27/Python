# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Jumbled Funny Names~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# split func
outline - 1. names input gheun list ready keli
2. eg jatin kumar ranchu - jatin first name, rest last name, need to separate it out.
using split function we will do this.(maxsplit pan use kravi lagel). jer func he kaam kernar asel ter it should return
first and last part of name, function fakt single item name ver run kraychy
3. firstnames chi ek list kruya main madhe ani same for last names
4. first names random.shuffle ne kruya shuffle in order
5. last names list brober zip kruya
'''

import random


def myFunc():
    return 0.1


def swapper(item):
    ls = item.split(" ", 1) #used maxsplit 1 - so that we get 2 elements, 1.fname and 2. lastname
    return ls


if __name__ == '__main__':
    friends = []
    fnames = []
    lnames = []
    num = int(input("Enter number of friends:\n"))
    print(f"Enter the name of your {num} friends:")

    for i in range(num):
        name = input(f"\n")
        friends.append(name)  # ithe list milali
    # print(friends)

    for friend in friends:
        lis = swapper(friend)
        fnames.append(lis[0])       #got fnames list here
        lnames.append(lis[1])       #got lnames list here

    random.shuffle(fnames, myFunc)
    res = [nm for nm in zip(fnames, lnames)]  #got list of tuples here which have 1st and last name
    # print(res)

    for item in res:
        final = " ".join(item)  #tuple che contents join zale with a space
        print(final)




# this solution is from youtube - shreya kapadia, best solution
'''
import random


def jumble_names():
    # If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
    # Thus in case of lname, even if someone has specified middle name it'll be considered as a whole
    fname = [name.split()[0] for name in names]  #very simple way to create list
    lname = [name.split(" ", 1)[1] for name in names]

    for _ in names:
        random_fname = random.choice(fname)
        random_lname = random.choice(lname)

        print(f"{random_fname} {random_lname}")

        fname.remove(random_fname)
        lname.remove(random_lname)


if __name__ == '__main__':
    n = int(input("Enter number of friends: "))
    names = []
    for i in range(n):
        names.append(input("Enter name of your friend: "))

    jumble_names()
'''
'''
#below is anohter approach (sidharth mallick):
def jumbleNames(cNames):
    # This is a function to Jumble Up the Names & Surnames
    split_names = []
    split_surnames = []
    for names in cNames:
        cNamesSplit = names.split(" ", 1)          # Splitting each cName into 2 parts
        split_names.append(cNamesSplit[0])      # Creating a list of only names
        split_surnames.append(cNamesSplit[1])   # Creating a list of only surnames
        split_surnames.reverse()                # Reversing the surname list inside the loop

    # Now creating the final list of JumbledUp Names & Surnames
    cJumbleNames = []
    for i in range(len(cNames)):
        cJumbleNames.append(split_names[i] + " " + split_surnames[i])

    return cJumbleNames


if __name__ == '__main__':
    cNames = []
    n = int(input("How many number of names to input? "))
    for i in range(n):
        cNames.append(input(f"{i+1}. Enter one name & Surname: "))
    print("Original List of Names:", cNames)

    cJumbleNames = jumbleNames(cNames)
    print("Jumbled List of Names :", cJumbleNames)
'''
