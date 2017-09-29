import random

def game():
    #assign a random number between 1 and 10 to a variable
    secret_num = random.randint(1,10)

    while True:
        #prompt user to guess a number between 1 and 10
        guess = user_prompt()
        #have the computer tell me whether its higher or lower
        number_compare(guess, secret_num)

def user_prompt():
    try:
        guess = int(input("What do you think my secret number is? "))
    except ValueError:
        print("That's not a number!")
        user_prompt()
    return guess


def number_compare(guess, secret_num):
    if guess > secret_num:
        print("too high!")
        return
    elif guess < secret_num:
        print("too low!")
        return
    elif guess == secret_num:
        print("Correct!")
        play_again()

def play_again():
    #ask to play again
    play_again = input("Do you want to play again? Y/n ")
    if play_again != 'n':
        game()
    else:
        exit()

game()
