import random

def guessing_game(min, max):
    # Generate a random number between 1 and 1000
    random_number = random.randint(min, max)
    
    # Keep track of the user's guesses and the hints
    user_guess = 0
    hints = 0
    
    while user_guess != random_number:
        # Ask the user to guess a number
        print(f"Guess a number between {min} and {max}: ")
        user_guess = int(input())
        
        # Check if the guess is too high or too low
        if user_guess > random_number:
            hints += 1
            print("Too high!")
        elif user_guess < random_number:
            hints += 1
            print("Too low!")
        
    
    # Scoring system
    else:
        print("Congratulations! You guessed the number.")
        # Print the number of hints used and score
        print(f"You used {hints} hints.")
        score = 105 - hints * 5
        if score < 1:
            score = 1
        print(f"Your score is {score}")

# Call the function
min = 1
max = 1000
guessing_game(min, max) 