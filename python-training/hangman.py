import random


def setup():
    word_list = ['one','two','three']
    #select word from word_list, set to lowercase, and add it as a list
    secret_word = []
    secret_word = list(word_list[random.randint(0,2)].lower())

    #build list with _s
    correct_guesses = []
    correct_guesses.extend('_' * len(secret_word))
    game(secret_word, correct_guesses)

#prompt and accept input
def prompt():
    guess = input("Enter a guess: ").lower()
    if len(guess) != 1:
        print("One character only, please!")
        prompt()
    return guess

#compare input to secret word
def compare_prompt(secret_word, guess, correct_guesses):
    for letter in secret_word:
        if guess == letter:
            #add letter to correct spot in status list by finding the index location in secret word
            correct_guesses[int(secret_word.index(letter))] = guess
            print("You got one!")

#output status
def output_status(correct_guesses):
    print(*correct_guesses)

def game(secret_word, correct_guesses):
    counter=0
    while correct_guesses!= secret_word:
        output_status(correct_guesses)
        guess = prompt()
        compare_prompt(secret_word,guess, correct_guesses)
        counter+=1
    print("You won! It took you {} guesses.".format(counter))

setup()
