import random
from ascii_art import get_snowman_stage

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """Plays the game."""
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []
    while True:
        # Checks if max mistakes have been made
        if mistakes == 4:
            print(f"Game Over! The word was: {secret_word}")
            get_snowman_stage(mistakes)
            ask_to_play_again()
        else:
            # show current snowman stage
            get_snowman_stage(mistakes)

            # DIsplay the word with guessed letters and underscores
            print("Word: ", end="")
            for char in secret_word:
                if char in guessed_letters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")

            # Get user input
            guess = input("\n\nGuess a letter: ").lower()

            # Check if the guess is valid
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            guessed_letters.append(guess)

            # Check if the guess is in the secret word
            if guess not in secret_word:
                mistakes += 1
            
        # Check if all letters have been guessed
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break

        # If word is fully guessed -> victory!
        if all_guessed:
            print(f"\nCongratulations, you saved the snowman! The word was: {secret_word}")
            get_snowman_stage(mistakes)
            ask_to_play_again()

def ask_to_play_again():
    """ Ask the user if they want to play again."""
    while True:
        try:
            play_again = input("Do you wanna play again (yes/no): ").lower()
            print("")
            if play_again == "yes":
                play_game()
                break  # exit the loop
            elif play_again == "no":
                print("Thanks for playing!")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please type 'yes' or 'no'.\n")