import random


def guessing_game():
    """Simple game to guess a number between 0 and 100

    Generate a random number from 0 up to and including 100,
    then keep guessing until the right number is found.
    """
    number = random.randint(0, 100)
    user_guess = -1
    print("Welcome to the guessing game, choose a number between 0 and 100")
    while user_guess != number:
        try:
            user_guess = int(input("Choose a number: "))
            if user_guess > number:
                print(f"{user_guess} is to high, try again")
            elif user_guess < number:
                print(f"{user_guess} is to low, try again")
        except ValueError:
            print("Incorrect value, choose numbers between 0 and 100")
            continue
    else:
        print(f"{number} is the correct number, thank you for playing!")


if __name__ == "__main__":
    guessing_game()
