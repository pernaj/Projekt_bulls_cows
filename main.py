# Programme creates secret 4-digit code on random basis.
# There cannot be zero at first position, no number can repeat.
import random

code = []

while len(code) < 4:
    number = random.randint(0, 9)
    if len(code) == 0 and number == 0:
        continue
    elif number in code:
        continue
    else:
        code.append(number)

# Programme greets the user and prints out introduction.
print("Hi there!","-" * 50, "I've generated a random 4 digit number for you.", 
      "Let's play a bulls and cows game.", "-" * 50, "Enter a number:", "-" * 50, sep="\n")
guess = input(">>> ")

# Guess number verification: correct length, only numbers, no zero at first position, no duplicity.
if len(guess) != 4:
    print("Incorrect length. Enter exactly 4 digit number!")
elif not guess.isdigit():
    print("Incorrect input. Enter only numbers!")
elif guess[0] == '0':
    print("Zero cannot be entered in the first position!")
elif len(guess) != len(set(guess)):
    print("Duplicity. The number cannot contain repeated digits!")
else:
    print("Entered number of correct length, containing only digits, with no zero " \
    "in the first position, without duplicity.", "Let's start the game", sep="\n")


