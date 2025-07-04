import random

play_again = "yes"

while play_again.lower() == "yes":
    magic_number = random.randint(1, 100)
    guess = -1
    guess_count = 0
    
    while guess != magic_number:
        guess = int(input("What is your guess? "))
        guess_count += 1
        
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print(f"You guessed it in {guess_count} guesses!")
    
    play_again = input("Do you want to play again? (yes/no): ")
