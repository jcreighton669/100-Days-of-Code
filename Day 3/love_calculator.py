# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
t_count = 0
r_count = 0
u_count = 0
e_count = 0
l_count = 0
o_count = 0
v_count = 0

names = name1.lower() + name2.lower()

t_count = names.count('t')
r_count = names.count('r')
u_count = names.count('u')
l_count = names.count('l')
o_count = names.count('o')
v_count = names.count('v')
e_count = names.count('e')

true_count = (t_count + r_count + u_count + e_count) * 10 
love_count = l_count + o_count + v_count + e_count
true_love = true_count + love_count

if true_love < 10 or true_love > 90: 
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50: 
    print(f"Your score is {true_love}, you are alright together.")
else: 
    print(f"Your score is {true_love}")