import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice_options = [rock, paper, scissors]
computers_choice = random.randint(0,2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

if (player_choice >=3 or player_choice < 0):
    print("You typed an invalid number. You Lose!")
else:
    print("""
______ _                         _____ _           _           
| ___ \ |                       /  __ \ |         (_)          
| |_/ / | __ _ _   _  ___ _ __  | /  \/ |__   ___  _  ___ ___  
|  __/| |/ _` | | | |/ _ \ '__| | |   | '_ \ / _ \| |/ __/ _ \ 
| |   | | (_| | |_| |  __/ |    | \__/\ | | | (_) | | (_|  __/ 
\_|   |_|\__,_|\__, |\___|_|     \____/_| |_|\___/|_|\___\___| 
                __/ |                                          
               |___/                                           """)

    print(choice_options[player_choice])

    print("""
 _____                             _              _____ _           _           
/  __ \                           | |            /  __ \ |         (_)          
| /  \/ ___  _ __ ___  _ __  _   _| |_ ___ _ __  | /  \/ |__   ___  _  ___ ___  
| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| | |   | '_ \ / _ \| |/ __/ _ \ 
| \__/\ (_) | | | | | | |_) | |_| | ||  __/ |    | \__/\ | | | (_) | | (_|  __/ 
 \____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|     \____/_| |_|\___/|_|\___\___| 
                      | |                                                       
                      |_|                                                       """)

    print(choice_options[computers_choice])
    is_draw = False
    did_player_win = False
    # choice_options = [rock, paper, scissors]

    if (player_choice == computers_choice):
        is_draw = True
    elif (player_choice == 0):
        if (computers_choice == 1): 
            did_player_win = False
        elif (computers_choice == 2):
            did_player_win = True
    elif (player_choice == 1):
        if (computers_choice == 0):
            did_player_win = True
        elif (computers_choice == 2):
            did_player_win = False
    elif (player_choice == 2):
        if (computers_choice == 0):
            did_player_win = False
        elif (computers_choice == 1):
            did_player_win = True

    if is_draw:
        print("""
______                    
|  _  \                   
| | | |_ __ __ ___      __
| | | | '__/ _` \ \ /\ / /
| |/ /| | | (_| |\ V  V / 
|___/ |_|  \__,_| \_/\_/  
                          
""")
    else:
        if did_player_win:
            print("""
______ _                         _    _ _           
| ___ \ |                       | |  | (_)          
| |_/ / | __ _ _   _  ___ _ __  | |  | |_ _ __  ___ 
|  __/| |/ _` | | | |/ _ \ '__| | |/\| | | '_ \/ __|
| |   | | (_| | |_| |  __/ |    \  /\  / | | | \__ \\
\_|   |_|\__,_|\__, |\___|_|     \/  \/|_|_| |_|___/
                __/ |                               
               |___/                                """)
        else: 
            print("""
 _____                             _              _    _ _           
/  __ \                           | |            | |  | (_)          
| /  \/ ___  _ __ ___  _ __  _   _| |_ ___ _ __  | |  | |_ _ __  ___ 
| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| | |/\| | | '_ \/ __|
| \__/\ (_) | | | | | | |_) | |_| | ||  __/ |    \  /\  / | | | \__ \\
 \____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|     \/  \/|_|_| |_|___/
                      | |                                            
                      |_|                                            """)
