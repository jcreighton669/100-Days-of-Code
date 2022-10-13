# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_person = random.randint(0, len(names)-1)
person_who_will_pay = names[random_person]
print(f"{person_who_will_pay} is going to buy the meal today.")