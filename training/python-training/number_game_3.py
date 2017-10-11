import random

secret_num = random.randint(1,10)

def main():
    counter = 0

    while counter < 6:
      guess = take_input()
      check_range(guess)
      input_eval(guess)
      counter+=1

    print("Too many guesses, you lose!")
    exit()

def take_input():
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("That's not a number! Try again...")
        take_input()
    return guess

def check_range(guess):
    if guess > 10:
        print("Thats too high! Try again...")
        take_input()
    elif guess <= 0:
        print("Thats too low! Try again...")
        take_input()
    else:
        return guess

def input_eval(guess):
    if guess == secret_num:
        print("You got it! The number was {}.".format(secret_num))
        exit()
        #It took you {} guesses".format(secret_num, counter))
    else:
        print("That's not it! Try again...")

    
main()
