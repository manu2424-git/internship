import random

WORDS = ["python", "hangman", "computer", "keyboard", "science"]
MAX_WRONG = 6

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")

    while wrong_guesses < MAX_WRONG:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        if guessed_letters:
            print("Guessed letters: " + ", ".join(guessed_letters))
        else:
            print("Guessed letters: none")
        print("Wrong guesses remaining: " + str(MAX_WRONG - wrong_guesses))

        try:
            guess = input("\nGuess a letter: ").lower().strip()
        except EOFError:
            print("\nNo input detected. Make sure you're running this in an "
                  "interactive terminal (e.g. 'python3 hangman.py' in a real "
                  "console), not a notebook cell or non-interactive runner.")
            return

        if guess == "":
            print("You didn't type anything. Please enter a letter.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_PICS[wrong_guesses])
                print("Word: " + display_word(word, guessed_letters))
                print("\nCongratulations! You guessed the word: " + word)
                return
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print(HANGMAN_PICS[wrong_guesses])
    print("You've run out of guesses! Game over.")
    print("The word was: " + word)


def main():
    while True:
        play_game()
        try:
            again = input("\nDo you want to play again? (y/n): ").lower().strip()
        except EOFError:
            print("\nNo input detected — exiting.")
            break
        if again != "y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()