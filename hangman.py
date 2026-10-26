import random

# Hangman stages: one stage for each number of incorrect guesses (0 to 6).
HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
    ======="""
]

# A small fallback list keeps the game playable without downloading a file.
FALLBACK_WORDS = [
    "python", "analytics", "computer", "hangman", "keyboard",
    "variable", "function", "database", "program", "developer","apple","mango","datheon"
]


def load_words(filename="words.txt"):
    """Load suitable words from words.txt, or use the fallback list."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha() and len(line.strip()) >= 3
            ]
        if words:
            return words
    except FileNotFoundError:
        pass

    return FALLBACK_WORDS


def display_game(secret_word, guessed_letters, incorrect_guesses):
    """Display the current gallows, word progress, and guessed letters."""
    print(HANGMAN_STAGES[incorrect_guesses])

    masked_word = " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print("\nWord:", masked_word)

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)).upper())
    else:
        print("Guessed letters: None")

    print(f"Incorrect guesses remaining: {6 - incorrect_guesses}")


def play_game():
    words = load_words()
    secret_word = random.choice(words)

    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("=" * 35)
    print("       HANGMAN WORD GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses available.")

    while incorrect_guesses < max_attempts:
        display_game(secret_word, guessed_letters, incorrect_guesses)

        # Check victory before asking for another letter.
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("Secret word:", secret_word.upper())
            return

        guess = input("\nEnter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter a single English letter (A-Z).")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

    # Show the final stage and the answer after six incorrect guesses.
    display_game(secret_word, guessed_letters, incorrect_guesses)
    print("\nGame over! Better luck next time.")
    print("The secret word was:", secret_word.upper())


if __name__ == "__main__":
    play_game()
