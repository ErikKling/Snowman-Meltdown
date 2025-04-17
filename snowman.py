import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def get_snowman_stage(stage):
    print(STAGES[stage])

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    mistakes = 0
    guessed_letters = []
    while True:
        if mistakes == 3:
            print(f"Game Over! The word was: {secret_word}")
            get_snowman_stage(mistakes)
            exit()
        else: 
            get_snowman_stage(mistakes)
            print("Word: ", end="")
            for char in secret_word:
                if char in guessed_letters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            guess = input("\n\nGuess a letter: ").lower()
            guessed_letters.append(guess)
            if guess in secret_word:
                print("Correct:", guess)
            else:
                mistakes += 1
    
if __name__ == "__main__":
    play_game()