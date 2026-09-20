import random

def number_guessing_game():
    print("=" * 40)
    print("  Welcome to the Number Guessing Game!  ")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 10.")
    
    # Generate a random integer between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            # Get player input
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            attempts += 1

            # Check conditions
            if guess < 1 or guess > 100:
                print("Out of bounds! Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()