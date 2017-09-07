import random

def setup():
    # setups the foundation of the game, selects a random word from a list
    # and instantiates variables

    word_list = ['one','two','three', 'teest']
    #select random word from word_list, set to lowercase, and add it as a list
    secret_word = []
    secret_word = list(word_list[random.randint(0,(len(word_list)-1))].lower())

    #build list with _s
    correct_guesses = []
    correct_guesses.extend('_' * len(secret_word))
    game(secret_word, correct_guesses)

def prompt():
    # prompts user for input and makes sure its only 1 character

    guess = input("Enter a guess: ").lower()
    if len(guess) != 1:
        print("One character only, please!")
        prompt()
    else:
        return guess

def compare_prompt(secret_word, guess, correct_guesses):
    # compares guessed letter to all letters in secret_word. when it finds a match it
    # updates the correct_guesses list and increments the found counter.
    # prints the found counter, letting the user know if (and how many) occurences they found
    counter = 0
    found = 0
    for letter in secret_word:
        if guess == letter:
            # counter trackers the index of the letter being compared, used to
            # record the occurnce in correct_guesses
            correct_guesses[counter] = guess
            found +=1
        counter +=1
    if found > 0:
        print("You got {}!".format(found))
    else:
        print("None of those, try again!")


def output_status(correct_guesses):
    #output progress tracking list
    print(*correct_guesses)

def game(secret_word, correct_guesses):
    # main function that controls flow of game

    counter=0
    while correct_guesses!= secret_word:
        output_status(correct_guesses)
        guess = prompt()
        compare_prompt(secret_word, guess, correct_guesses)
        counter+=1
    print("You won! It took you {} guesses.".format(counter))
    output_status(correct_guesses)
    play_again()


def play_again():
    play_again = input("\nDo you want to play again? Y/n ")
    if play_again != 'n':
        setup()
    else:
        exit()

setup()
