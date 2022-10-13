#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

coin_value = random.randint(1,101) % 2

if coin_value == 1:
    print("Heads")
else: 
    print("Tails")
