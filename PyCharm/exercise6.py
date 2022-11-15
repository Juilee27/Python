#snake water gun game dvpt - s w g , play for only 10 times using while, keep score of
# computer vs user #use random module for computer
# after while loop is over on basis of score declare winner

import  random

you = []
comp = []
def game(system, user):
    if system== 'snake' and user == 'gun':
        you.append('won')  # print("user won!")
    elif system == 'water' and user == 'snake':
        you.append('won')  # print("user won!")
    elif system == 'gun' and user == 'water':
        you.append('won')  # print("user won!")
    elif system == user:
        # print('it is a tie')
        pass
    else:
        comp.append('won')  # print("user lost the game!")

num = int(input('enter no of times you wanna play: '))
j=0
while j <num:
    rand = ['snake', 'water', 'gun']
    sys_choice = random.choice(rand)
    # print(sys_choice)
    inp = input('enter your choice from snake, water, gun: ')
    inp = inp.lower()
    game(sys_choice, inp)
    j+=1
user_count = you.count('won')
comp_count = comp.count('won')
if user_count > comp_count:
    print(f'user won {user_count} times')
elif user_count == comp_count:
    print('it is a draw')
else:
    print(f'computer won {comp_count} times')













