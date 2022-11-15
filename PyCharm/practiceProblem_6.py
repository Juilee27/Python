# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Guess The Number~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random

def guessTheNum(g):
    trials = 0
    while g != num:
        if g < num:
            print(f"Wrong, guess a greater number again")
            g = int(input())
            trials += 1
        elif g > num:
            print(f"Wrong, guess a smaller number again")
            g = int(input())
            trials += 1
        # continue  ~NOTE- continue is redundant here
    trials += 1
    print(f"Correct, you took {trials} trials to guess the number")
    return trials

if __name__ == '__main__':
    try:
        a = int(input("Enter the value of a\n"))
        b = int(input("Enter the value of b\n"))
        #range limits taken from user
        num = random.randint(a, b)
        #random num chosen by interpretor in range provided
        print(num)

        print(f"Player 1:\nPlease guess the number between {a} and {b}.")
        #player 1 guess input
        guess_1 = int(input())
        t1 = guessTheNum(guess_1)

        print(f"Player 2:\nPlease guess the number between {a} and {b}.")
        #player 2 guess input
        guess_2 = int(input())
        t2 = guessTheNum(guess_2)

        if t1 > t2:
            print("Player 2 wins!")

        elif t1 < t2:
            print("Player 1 wins!")

        else:
            print("It is a TIE!")

    except ValueError:
        print("please enter valid integer.")
