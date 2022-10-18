import random
from hangman_art import logo, stages
from hangman_words import word_list

end_of_game = False
mystery_word = random.choice(word_list)
lives = 6

print(logo)

display = []
word_length = len(mystery_word)
incorrect_letters = []
guessed_letters = []

for i in range(word_length):
    display += '_'
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = mystery_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in mystery_word:
        lives = lives - 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if guess not in incorrect_letters:
          incorrect_letters.append(guess)
    

    print(stages[lives])
    print(f"Incorrectly guessed letters {incorrect_letters}")
        
    if '_' not in display:
        print("Congratulations, You WIN!")
        break
    if lives == 0:
        print("Game Over!")
        print(f"The mystery word was {mystery_word}")
        break
    print(f"{''.join(display)}")
