import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "random", "program", "simple"]
    word = random.choice(words)  # Choose a random word
    guessed_word = ["_"] * len(word)  # Display blanks
    guessed_letters = []  # Track guessed letters
    attempts = 6  # Wrong guess limit

    print(" Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", attempts, "lives.")

    while attempts > 0 and "_" in guessed_word:
        print("\nCurrent word:", " ".join(guessed_word))
        print("Guessed letters:", " ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print("Wrong guess! Lives left:", attempts)

    # End of game
    if "_" not in guessed_word:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()