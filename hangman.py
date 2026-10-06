"""
CodeAlpha — Task 1: Hangman Game
Intern project: text-based Hangman with 5 predefined words and 6 wrong guesses.
Key concepts: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "alpha", "code", "script", "intern"]
MAX_WRONG = 6


def display_state(secret, guessed, wrong):
    shown = " ".join(letter if letter in guessed else "_" for letter in secret)
    print("\nWord:  ", shown)
    print("Guessed:", " ".join(sorted(guessed)) if guessed else "(none)")
    print(f"Wrong guesses left: {MAX_WRONG - wrong}")


def play():
    secret = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can miss {MAX_WRONG} times.")

    while wrong < MAX_WRONG:
        display_state(secret, guessed, wrong)

        if all(letter in guessed for letter in secret):
            print(f"\nYou won. The word was '{secret}'.")
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already tried that letter.")
            continue

        guessed.add(guess)
        if guess not in secret:
            wrong += 1
            print("Wrong.")
        else:
            print("Correct.")

    display_state(secret, guessed, wrong)
    print(f"\nYou lost. The word was '{secret}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()
