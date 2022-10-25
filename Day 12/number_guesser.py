#Number Guessing Game Objectives:
from random import randint
from art import logo


NUMBER_OF_HARD_GUESSES = 5
NUMBER_OF_EASY_GUESSES = 10



def compare_answer(guess, answer, turns):
    """Return the number of turns left after a guess in made."""
    if guess > answer: 
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else: 
        print(f"You got it! the answer was {answer}.")

def set_difficulty():
    """Sets the number of guesses depending on the difficulty selected."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return NUMBER_OF_EASY_GUESSES
    else: 
        return NUMBER_OF_HARD_GUESSES

def play_game():
    """Runs the game for the user to interact with."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mystery_number = randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != mystery_number:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = compare_answer(guess, mystery_number, turns)
        if turns == 0: 
            print("You've run out of guesses, you lose.")
            return
        elif guess != mystery_number:
            print("Guess again.")


play_game()