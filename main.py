# Programme greets the user and prints out introduction.
print("Hi there!","-" * 50, "I've generated a random 4 digit number for you.", 
      "Let's play a bulls and cows game.", "-" * 50, "Enter a number:", "-" * 50, sep="\n")

# Programme creates secret 4-digit number on random basis.
import random

secret_number = []

while len(secret_number) < 4:
    digit = random.randint(0, 9)
    secret_number.append(digit)
print(secret_number)