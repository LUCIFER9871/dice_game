import random
print("HI Welcome to throw dice game, Lets start game")
roll_dice= random.randrange(1,6)
chance = 2
guess_counter = 0
while guess_counter < chance:
    guess_counter += 1
    my_guess = int(input("Throw your dice: " ))


    if my_guess == roll_dice:
        print(f'The number is {roll_dice} and you found it right !! in the {guess_counter} attempt')
        break 
    elif guess_counter >= chance and my_guess != roll_dice:
        print(f'oops sorry, the number is {roll_dice}better to next time')
    elif my_guess > roll_dice:
        print('Your guess is higher')
    
    elif my_guess < roll_dice :
        print('your dice is lesser')
