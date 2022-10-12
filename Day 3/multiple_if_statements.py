print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can rid the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        print("Children's tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is {bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")
