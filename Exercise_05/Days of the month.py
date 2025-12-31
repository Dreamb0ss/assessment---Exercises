months = {  
    1: 31, 2: 28, 3: 31, 4: 30,   # days in each month
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Enter month number (1-12): "))  
# ask user to enter a month number

if month == 2:  
    # special case for February
    leap = input("Is it a leap year? (yes/no): ").lower()  
    # ask if it is a leap year
    if leap == "yes":
        print("29 days")  
        # February has 29 days in a leap year
    else:
        print("28 days")  
        # February has 28 days in a normal year
elif month in months:
    print(f"{months[month]} days")  
    # print days for the selected month
else:
    print("Invalid month")  
    # handle invalid month numbers
