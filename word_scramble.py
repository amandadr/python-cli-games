import random
import time

"""
Make sure to generate words.txt using generate_word_list.py
"""

def random_words():
    with open("words.txt", "r") as file:
      words = file.read().splitlines()
    return words

def choose_word_to_scramble(words):
    index = random.randint(0, len(words) - 1)
    return words[index]

def scramble_word(word):
    scrambled_word = ''
    while len(word) > 0:
        index = random.randint(0, len(word) - 1)
        letter = word[index]
        scrambled_word += letter
        word = word[:index] + word[index + 1:]
    return scrambled_word

def get_player_guess():
    print("Enter your guess: ")
    guess = input()
    return guess

def check_guess(guess, word):
    if guess.lower() == word.lower():
        return True
    else:
        return False

def update_score(score, correct):
    if correct:
        score += 1
    return score

# Main function
def main():
    # Initialize variables
    words = random_words()
    time_limit = 60  # Set the time limit to 1 minute
    score = 0  # Initialize score
    current_word = choose_word_to_scramble(words)
    scrambled_word = scramble_word(current_word)

    print("Welcome to the Word Scramble Game!")
    print("You have", time_limit, "seconds to unscramble as many words as possible, good luck!")
    print("Scrambled word:", scrambled_word)

    start_time = time.time()
    while time.time() - start_time < time_limit:
        guess = get_player_guess()
        correct = check_guess(guess, current_word)
        if correct:
            print("Correct!")
            current_word = choose_word_to_scramble(words)
            scrambled_word = scramble_word(current_word)
            print("Scrambled word:", scrambled_word)
        else:
            print("Incorrect. Try again.")
        score = update_score(score, correct)

    print("Time is up!")
    print("You scored ", score, " points.")
    # Scoring system
    if score > 5:
        print("Congratulations! You are a word scramble master!")
    else:
        print("Better luck next time! Keep practicing.")

# Call the main function
if __name__ == "__main__":
    main()