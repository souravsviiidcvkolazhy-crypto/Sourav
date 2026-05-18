import random


def play_guess_the_number():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to Guess the Number.")
    print("I am thinking of a number between 1 and 100.")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Take a guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low. Try again.")
        elif guess > secret:
            print("Too high. Try again.")
        else:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts.")
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    play_guess_the_number()
