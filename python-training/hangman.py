import random
#pick a random word from a list
#user guesses letters in the word
list = ['one','two','three']

def main():
    secret_word = list[random.randint(1,2)]
    correct_guesses = []
    i=0
    #build list with _s
    while i < len(secret_word):
        correct_guesses.append('_')
        i+=1

#compare lists and print correct_guesses list
while letter in secret_word
    if secret_word[letter] == correct_guesses[letter]:
        print("yes")
    else:
        print("no")


#print(*correct_guesses)


#status()

#let user guess a letter
#evaluate whether letter is in the word
#if it is, output the # of letters guessed correctly - total length


#def status()
