import random
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def setup():
    # setups the foundation of the game, selects a random word from a list
    # and instantiates variables
    word_list = []
    bad_guesses = []

    #read word list from file into list var
    filename = "word_file.txt"
    file = open(filename, "r")
    for word in file:
        #make sure to strip the trailing \n
        word_list.append(word.rstrip('\n'))
    print(*word_list)
    #select random word from word_list, set to lowercase, and add it as a list
    secret_word = []
    secret_word = list(word_list[random.randint(0,(len(word_list)-1))].lower())
    print(secret_word)
    #build progress tracking list with _s
    correct_guesses = []
    correct_guesses.extend('_' * len(secret_word))
    game(secret_word, correct_guesses, bad_guesses)

def prompt():
    # prompts user for input and makes sure its only 1 character
    guess = input("Enter a guess: ").lower()
    if len(guess) != 1:
        print("One character only, please!")
        return None
    else:
        return guess

def compare_prompt(secret_word, guess, correct_guesses,bad_guesses):
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
        bad_guesses.append(guess)

        #print(guess)


def output_status(correct_guesses, bad_guesses):
    #output progress tracking list
    clear()
    print("\n","\n")
    if bad_guesses != []:
        print(*bad_guesses)
    print("\n","\n")
    print(*correct_guesses)


def game(secret_word, correct_guesses, bad_guesses):
    # main function that controls flow of game and monitors for a win
    # counter tracks the amount of guesses and reports to user at the end

    counter=0
    while correct_guesses!= secret_word:
        output_status(correct_guesses, bad_guesses)
        guess = prompt()
        if guess == None:
            guess = prompt()
        compare_prompt(secret_word, guess, correct_guesses, bad_guesses)
        counter+=1
    print("You won! It took you {} guesses.".format(counter))
    output_status(correct_guesses, bad_guesses)
    play_again()


def play_again():
    play_again = input("\nDo you want to play again? Y/n ")
    if play_again != 'n':
        setup()
    else:
        exit()

setup()
