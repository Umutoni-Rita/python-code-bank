import random

def number_guessing():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("---Welcome to the Number Guessing Game---")
    print("I've picked a number between 1 and 20. GUess it!")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

number_guessing()