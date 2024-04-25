import random
import string

def generate_random_word(length, start_letter=None):
    if start_letter:
        start_letter = start_letter.lower()
    else:
        start_letter = random.choice(string.ascii_lowercase)

    if length < 1:
        raise ValueError("Length should be at least 1")

    word = start_letter

    while len(word) < length:
        next_char = random.choice(string.ascii_lowercase)
        word += next_char

    return word

# Example usage:
try:
    word_length = int(input("Enter the desired word length: "))
    start_char = input("Enter the desired starting letter (or press Enter for a random starting letter): ")

    random_word = generate_random_word(word_length, start_char)
    print(f"Random word: {random_word}")

except ValueError as e:
    print(f"Error: {e}")