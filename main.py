import random

# Constant: given lenght of the secret code; 
# to be easily changed throughout the programme, should there be such a need.

CODE_LENGTH = 4

# Programme greets the user and prints out introduction.

print("Hi there!","-" * 50, 
      f"I've generated a random {CODE_LENGTH} digit number for you.", 
      "Let's play a bulls and cows game.", "-" * 50, "Enter a number:", 
      "-" * 50, sep="\n")

# Programme randomly generates secret 4-digit number; 
# no zero in the first position; no duplicity.

code = []
while len(code) < CODE_LENGTH:
    number = random.randint(0, 9)
    if len(code) == 0 and number == 0:
        continue
    elif number in code:
        continue
    else:
        code.append(number)

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
    print("bulls, cows...")

guess = input(">>> ")
