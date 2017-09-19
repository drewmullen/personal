word = "TesTaeiou"

def disemvowel(word):

    word = list(word.lower())
    for letter in word:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            word.remove(letter)
    print(*word)
    return ''.join(word)

print(disemvowel(word))
