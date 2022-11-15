# take n =18
# number of guesses - 9
# print no of guesses left
# no of guesses it took to finish
# game over

n = 18
guesses = 9
i = 0
for i in range(0,9):
    print('guess the number in 1 to 100: ')
    inp = int(input())

    if inp < n:
        print("no is lesser, try again ")
    elif inp > n:
        print("no is greater, try again ")
    elif inp == n:
        print('number correctly guessed!\nnumber of guesses taken to finish are: ',i+1)
        break
    print('number of guess left: ', 9-(i+1))
