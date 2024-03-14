import nltk
import random

nltk.download('words')

def generate_word_list(min_length, max_length):
    words = set(nltk.corpus.words.words())
    #  Use the basic English basic word list to ensure common words
    common_words = set(word.lower() for word in nltk.corpus.words.words() if word.lower() in nltk.corpus.words.words('en-basic'))
    filtered_words = [word.lower() for word in words if min_length <= len(word) <= max_length and word.lower() in common_words]
    return filtered_words

def save_words_to_file(words, filename):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')

# Adjust these parameters as desired to adjust difficulty
min_length = 3   # Minimum length of words
max_length = 6   # Maximum length of words

words = generate_word_list(min_length, max_length)
save_words_to_file(words, 'words.txt')
print("Word list generated and saved to 'words.txt'")
