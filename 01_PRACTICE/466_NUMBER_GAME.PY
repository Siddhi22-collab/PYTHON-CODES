import random

number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("You win!")
else:
    print("You lose! The number was", number)