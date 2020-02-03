import random

theNumber = random.randint(1, 26)
print("I'm thinking of a number between 1 and 25.")
print("Try to guess the number I'm thinking.")

for guesses in range(0, 10):
    try:
        guess = input()

        if int(guess) < theNumber:
            print("Your guess is too low. You have " + str(10 - guesses) + " left.")
        elif int(guess) > theNumber:
            print("Your guess is too high. You have " + str(10 - guesses) + " left.")
        else:
            break

        #guesses = guesses + 1  

    except:
        print("Please type a number.")

if int(guess) == theNumber:
    print("Good job! You guessed the number in " + str(guesses) + " guesses.")
else:
    print("You guessed incorrectly. The number was " + str(theNumber) + ".")

    