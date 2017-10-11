import random

secret_num = random.randint(1,10) #generates a # between 1 and 10
counter = 0

while True:
  guess = int(input("guess a number between 1 and 10: "))
  counter+=1
  if guess == secret_num:
    print("You got it! The number was {}. It took you {} guesses".format(secret_num, counter))
    break
  else:
    print("That's not it!")
