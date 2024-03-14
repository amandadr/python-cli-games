import random
"""
Make sure to generate words.txt using generate_word_list.py
"""

def choose_word():
    # Generate a random word from the given word list
    with open("words.txt", "r") as file:
      words = file.read().splitlines()
    return random.choice(words)

def display_word(word, guessed_letters):
    # Print the hidden word using dashes and guesses using letters
    print("-" * (len(word) + 5))
    for i in range(len(word)):
        if word[i] in guessed_letters:
            print(word[i], end="")
        else:
            print("-", end="")
    print(" ", end=" ")
    return

def check_guess(guess, guessed_letters):
    # Check if the guess is valid and not already guessed
    if guess in "abcdefghijklmnopqrstuvwxyz":
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("Guessed letters:", guessed_letters)
            return True
        else:
            print("That letter has already been guessed.")
            return False
    else:
        print("Invalid guess. Guess a letter from the alphabet.")
        return False

def update_display(word, guessed_letters):
    # Update the display with current guesses
    display_word(word, guessed_letters)

def is_game_over(word, guessed_letters, guess_count, guess_limit):
    # Check if the player has guessed all the letters or exceeded the limit
    if all(word[i] in guessed_letters for i in range(len(word))):
        print(f"Congratulations! You win with {guess_limit - guess_count} guesses left!")
        return True
    elif guess_count == {guess_limit}: # Set the guess limit here
        print(f"You lose! The word was '{word}'")
        return True
    else:
        return False

def play_hangman(guess_limit):
    word = choose_word()
    guessed_letters = []
    guess_count = 1
    print(f"You have {guess_limit} guesses to guess the word.")
    while not is_game_over(word, guessed_letters, guess_count, guess_limit):
        print("Guess a letter:")
        guess = input().lower()
        if check_guess(guess, guessed_letters):
            update_display(word, guessed_letters)
            guess_count += 1
        else:
            print("\n")
    return

play_hangman(guess_limit=12)