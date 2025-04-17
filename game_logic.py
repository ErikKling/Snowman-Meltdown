import random
from ascii_art import get_snowman_stage

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []
    while True:
        if mistakes == 3:
            print(f"Game Over! The word was: {secret_word}")
            get_snowman_stage(mistakes)
            ask_to_play_again()
        else: 
            get_snowman_stage(mistakes)
            print("Word: ", end="")
            for char in secret_word:
                if char in guessed_letters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            guess = input("\n\nGuess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            guessed_letters.append(guess)


            if guess not in secret_word:
                mistakes += 1
            
        # Check if all letters have been guessed
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break

        if all_guessed:
            print(f"\nCongratulations, you saved the snowman! The word was: {secret_word}")
            get_snowman_stage(mistakes)
            ask_to_play_again()

def ask_to_play_again():
    while True:
        try:
            play_again = input("Do you wanna play again (yes/no): ").lower()
            print("")
            if play_again == "yes":
                play_game()
                break  # Wichtig, damit die Schleife nicht ewig weiterläuft
            elif play_again == "no":
                print("Thanks for playing!")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please type 'yes' or 'no'.\n")