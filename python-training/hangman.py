import random
#pick a random word from a list
#user guesses letters in the word
word_list = ['one','two','three']

def main():
    #select word from word_list, set to lowercase, and add it as a list
    secret_word = []
    secret_word = list(word_list[random.randint(1,2)].lower())

    #build list with _s
    correct_guesses = []
    correct_guesses.extend('_' * len(secret_word))

#accept input
def prompt():
    guess = input("Enter a guess: ").lower()
    return guess

#compare input to secret word
def compare_prompt(secret_word, guess):
    for letter in secret_word:
        if guess == letter:
            #add letter to correct spot in status list by finding the index location in secret word
            correct_guesses[int(secret_word.index(letter))] = guess
            #find index of letter in secret_word and make correct_guesses correlating index the guess

#output status
    #print(*correct_guesses)
