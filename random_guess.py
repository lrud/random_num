import random

random_num = random.randint(1,100)
user_num = input('Guess the random number between 1 and 100: ')

active = True
while active:
    if int(user_num) != random_num:
        if int(user_num) < random_num:
            # print('Guess Higher!')
            user_num = input('Guess Higher! ')
        else:
            # print('Guess Lower!')
            user_num = input('Guess Lower! ')
    else:
        print(f"You correctly guessed the number: {random_num}!")
        active = False