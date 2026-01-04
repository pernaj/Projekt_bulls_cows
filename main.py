import random

from _collections_abc import Iterable, Callable

# Constant: given lenght of the secret code; 
# to be easily changed throughout the programme, should there be such a need.

CODE_LENGTH = 4

# Programme greets the user and prints out introduction.

print("Hi there!","-" * 50, 
      f"I've generated a random {CODE_LENGTH} digit number for you.", 
      "Let's play a bulls and cows game.", "-" * 50, "Enter a number:", 
      "-" * 50, sep="\n")

# Programme randomly generates secret number; 
# 4 digits, no zero in the first position, no duplicity.

code = []
while len(code) < CODE_LENGTH:
    number = random.randint(0, 9)
    if len(code) == 0 and number == 0:
        continue
    elif number in code:
        continue
    else:
        code.append(number)

# Auxiliary functions to validate if initial conditions for guessed number are fulfilled:
# correct length, only numbers, no zero at first position, no duplicity.

def check_length(x: str) -> str | None:
    """ Validates if the entered number has correct length.
    Returns error message or None.
    """
    if len(x) != CODE_LENGTH:
        return f"Error: invalid length. Enter exactly {CODE_LENGTH} digit number!"
    return None

def check_digits(x: str) -> str | None:
    """Validates if the entered number contains only digits.
    Returns error message or None.
    """
    if not x.isdigit():
        return f"Error: entered no digits. Only digits are allowed!"
    return None

def check_zero(x: str) -> str | None:
    """Validates if there is no zero in the first position of the entered number.
    Returns error message or None.
    """
    if not x:
        return f"Error: empty input. Enter exactly {CODE_LENGTH} digit number!"
    if x[0] == '0':
        return f"Error: leading zero. Zero cannot be entered in the first position!"
    return None

def check_duplicity(x: str) -> str | None:
    """Validates if there are only unique numbers in the entered number.
    Returns error message or None.
    """
    if len(x) != len(set(x)):
        return f"Error: duplicity. The number cannot contain repeated digits!"
    return None 

# Main function to validate the guessed number using output of auxiliary functions.

def validate_guess(x: str, validators: Iterable[Callable[[str], str | None]]) -> tuple[bool, list[str]]:
    """Calls all functions from 'validators' over parameter x.
    Returns pair ok, errors, where:
    - ok: True/False if there is not/is found error.
    - errors: list of error messages. Empty list = no errors, input is valid.
    """
    errors = []
    for fn in validators:
        msg = fn(x)
        if msg:
            errors.append(msg)
    ok = len(errors) == 0
    return ok, errors

validators = [check_length, check_digits, check_zero, check_duplicity]

# Function counting number of bulls and cows.

def get_bulls_cows(secret_nr: list[int], guessed_nr: str) -> tuple[int, int]:
    """Gets number of bulls and cows by comparison of secret number with guessed number.
    Returns collection of bulls (correct number at correct position)
    and cows (correct number at wrong position).
    At first counts number of bulls, then sorts remaining numbers (no-bulls),
    and compares no-bulls numbers with each other."""
    list_guess = [int(x) for x in guessed_nr]  
    bulls = sum(1 for bull in range(CODE_LENGTH) if secret_nr[bull] == list_guess[bull])
    cows = 0

    remaining_secret = []
    remaining_guessed = []
    for x in range(CODE_LENGTH):
        if secret_nr[x] != list_guess[x]:
            remaining_secret.append(secret_nr[x])
            remaining_guessed.append(list_guess[x])

    for number in remaining_guessed:
        if number in remaining_secret:
            cows += 1
            remaining_secret.remove(number)
    
    return bulls, cows

# Programme gets user's input, validates it and if ok, counts bulls and cows.
# If necessary, looped.

while True:
    while True:
        guess = input(">>> ")

        ok, errors = validate_guess(guess, validators)
        if ok:
            break
        else: 
            for e in errors:
                print(e)
            print("Try again.")
    
    bulls, cows = get_bulls_cows(code, guess)

    bull_label = "bull" if bulls == 1 else "bulls"
    cow_label = "cow" if cows == 1 else "cows"

    print(f"{bull_label}: {bulls}, {cow_label}: {cows}")

    if bulls == CODE_LENGTH:
        print("Correct, you've guessed the right number", 
              "-"*50, "That's amazing!", sep="\n")
        break
    else:
        print("Not yet. Guess again...", "-"*50, sep="\n")



