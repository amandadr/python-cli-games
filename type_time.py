import random
import time

"""
CONSTANTS
"""
time_limit = 30

# Make sure words.txt is generated using generate_word_list.py
def generate_random_words(time_limit):
    start_time = time.time()
    while time.time() - start_time < time_limit:
        yield random.choice(open("words.txt", "r").read().splitlines())

def display_instructions():
    print("Welcome to the Type Time Speed Challenge!")
    print(f"You will have {time_limit} seconds to type as many words as possible.")
    print("Your typing speed and accuracy will be calculated at the end.")
    print("Type the words as they appear on the screen and press 'Enter' after each word.")
    print("Press 'Enter' to start the game.")
    input()

# The primary game function
def typing_test(word_list):
    start_time = time.time()
    original_words = ''
    typed_words = ''
    for word in word_list:
        print(word, end='')
        original_words += word + ' '
        typed_word = input(' ')
        typed_words += typed_word + ' '
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    num_typed_words = len(typed_words.split())
    print(f"\nYou have typed {num_typed_words} words in {elapsed_time} seconds.")
    calculate_typing_score(original_words, typed_words, num_typed_words, elapsed_time)
    print("Thank you for playing!")

# Calculate the typing speed (WPM) and accuracy
def calculate_typing_score(original_words, typed_words, num_typed_words, elapsed_time):
  # Calculate words per minute (WPM)
  num_characters = len(' '.join(typed_words))
  wpm = (num_characters / 5) / (elapsed_time / 60)
  
  # Calculate accuracy
  typed_words_list = typed_words.split()
  original_words_list = original_words.split()
  num_correct_words = sum([1 for i in range(num_typed_words) if typed_words_list[i] == original_words_list[i]])
  accuracy = (num_correct_words / num_typed_words) * 100
  
  # Display results
  print("\n--- Results ---")
  print(f"Time: {elapsed_time:.2f} seconds")
  print(f"Words per minute: {wpm:.2f} WPM")
  print(f"Accuracy: {accuracy:.2f}%")

# Main function: game logic
def main():
    word_generator = generate_random_words(time_limit)
    display_instructions()
    typing_test(word_generator)

if __name__ == "__main__":
    main()