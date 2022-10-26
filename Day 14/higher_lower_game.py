from art import logo, vs
from game_data import data
from random import choice


def display_logo():
    """Print the logo for the High-Low Game."""
    print(logo)


def display_vs_symbol():
    """Print the VS symbol."""
    print(vs)


def get_random_person():
    """Returns a randomly selected entity from the data."""
    person = choice(data)
    return person


def display_person_data(person):
    """Returns the person data formatted into a easier to read string."""
    return f"{person['name']}, {person['description']}, from {person['country']}."


def confirm_different_entities(person_a, person_b):
    """Confirms that the two options are different."""
    if person_a != person_b:
        return True
    else:
        person_b = get_random_person()
        confirm_different_entities(person_a, person_b)


def more_popular_stays(person_a, person_b):
    """Returns the more popular person when correct guess happens."""
    person_to_stay = person_a
    if person_a["follower_count"] > person_b["follower_count"]:
        person_to_stay = person_a
    else:
        person_to_stay = person_b
    return person_to_stay



def more_popular(person_a, person_b):
    """Asks the user to guess the more popular person/group. Returns true for correct guess and false for incorrect guess."""
    more_popular_person = 'Z'
    display_logo()
    print("Confirm A:" + display_person_data(person_a))
    display_vs_symbol()
    print("Against B: " + display_person_data(person_b))
    if person_a["follower_count"] > person_b["follower_count"]:
        more_popular_person = 'A'
    else:
        more_popular_person = 'B'
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == more_popular_person:
        return True
    else:
        return False


def play_game():
    """Runs the games and calls the necessary functions."""
    is_correct_answer = True
    score_counter = 0
    entity_a = get_random_person()
    while is_correct_answer:
        entity_b = get_random_person()

        if confirm_different_entities(entity_a, entity_b):
            is_correct_answer = more_popular(entity_a, entity_b)
            if is_correct_answer:
                score_counter += 1
                print(f"You're right! Current score: {score_counter}")
                entity_a = more_popular_stays(entity_a, entity_b)
                entity_b = get_random_person()
            else:
                print("Game Over")


play_game()