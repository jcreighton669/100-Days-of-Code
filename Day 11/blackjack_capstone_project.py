import random
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)    
    return card


def calculate_score(cards_in_hand):
    """Returns the value of a list of cards."""
    value = sum(cards_in_hand)
    if len(cards_in_hand) == 2 and value == 21:
        return 0
    if 11 in cards_in_hand and value > 21:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)
        value = sum(cards_in_hand)
    return value


def compare(user_score, computer_score):
    if user_score == computer_score:
        return f"The hand is a draw. The score is {user_score}"
    elif computer_score == 0:
        return "The computer has won the hand with a blackjack"
    elif user_score == 0:
        return "The user has won the hand with blackjack"
    elif user_score <= 21 and computer_score <= 21:
        if user_score > computer_score: 
            return f"The user won the hand with {user_score} against the computer's score of {computer_score}"
        if computer_score > user_score:
            return f"The user lost the hand with {user_score} against the computer's score of {computer_score}"
    elif user_score > 21: 
        return "The player busts and the computer wins"
    elif computer_score > 21:
        return "The computer busts and the player wins"


def play_hand(): 
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"->  Your cards: {user_cards} --> current score: {user_score}")
        print(f"->  Computers 1st card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else: 
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                is_game_over = True

    print(compare(user_score, computer_score))


play_another_hand = True

while play_another_hand:
    play_again = input("Type 'y' to play another hand or type 'n' to leave the table: ")
    if play_again == 'n':
        play_another_hand = False
    else: 
        print(logo)
        play_hand()

