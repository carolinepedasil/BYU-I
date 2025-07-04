# I added a random word selection from a list of words.
# I limited the number of guesses to 6 to increase difficulty.

import random

# List of possible secret words
words_list = ["mosiah", "temple", "moroni", "nephi", "helaman"]

secret_word = random.choice(words_list)

guess = ""
num_guesses = 0
max_guesses = 6
hint = ["_"] * len(secret_word)

print("Welcome to the word guessing game!")
print("Your hint is: ", " ".join(hint))

while guess != secret_word and num_guesses < max_guesses:
    guess = input("What is your guess? ").lower()
    num_guesses += 1

    if len(guess) != len(secret_word):
        print(f"Sorry, the guess must have {len(secret_word)} letters.")
        continue

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint[i] = guess[i].upper()
        elif guess[i] in secret_word:
            hint[i] = guess[i].lower()
        else:
            hint[i] = "_"

    print("Your hint is: ", " ".join(hint))

    if guess == secret_word:
        print(f"Congratulations! You guessed it in {num_guesses} guesses.")
    elif num_guesses == max_guesses:
        print(f"Sorry, you've reached the maximum number of guesses. The word was '{secret_word}'.")

if guess != secret_word and num_guesses >= max_guesses:
    print(f"Game Over! You didn't guess the word in {max_guesses} guesses.")
