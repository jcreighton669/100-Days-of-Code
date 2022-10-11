#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))
number_of_checks = int(input("How many people to split the bill? "))

tip_percentage /=100

each_check = ((total_bill / number_of_checks) * (1 + tip_percentage))

check_with_cents = round(each_check, 2)

print(f"Each person whould pay: ${check_with_cents}")
