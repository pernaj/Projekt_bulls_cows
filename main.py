import random

# Constant: given lenght of the secret code; 
# to be easily changed throughout the programme, should there be such a need.

CODE_LENGTH = 4

# Programme greets the user and prints out introduction.

print("Hi there!","-" * 50, 
      f"I've generated a random {CODE_LENGTH} digit number for you.", 
      "Let's play a bulls and cows game.", "-" * 50, "Enter a number:", 
      "-" * 50, sep="\n")

# Programme randomly generates secret number; 
# 4 digits, no zero in the first position; no duplicity.

code = []
while len(code) < CODE_LENGTH:
    number = random.randint(0, 9)
    if len(code) == 0 and number == 0:
        continue
    elif number in code:
        continue
    else:
        code.append(number)

# Functions to validate if initial conditions for guessed number are fulfilled:
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


guess = input(">>> ")
