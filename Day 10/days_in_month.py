def is_leap(year):
    """Return if a provided year is a Leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year_input, month_input):
    """Return the number of days in a month depending on the year and month provided"""
    if month_input < 0 or month_input > 12:
        return
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    is_leap_year = is_leap(year_input)
    if is_leap_year and month_input == 2:
        return month_days[month_input-1] + 1
    return month_days[month_input-1]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












