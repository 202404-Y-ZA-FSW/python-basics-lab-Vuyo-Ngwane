import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number_game():
    number_to_guess = generate_random_number()
    attempts = 0
    guess = None
    
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")
            
if __name__ == "__main__":
    guess_number_game()

    