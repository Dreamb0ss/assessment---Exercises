name = input("Enter your name: ")        # ask user for name
hometown = input("Enter your hometown: ")  # ask user for hometown

while True:                              # loop until valid age is entered
    try:
        age = int(input("Enter your age: "))  # convert age to integer
        break                            # exit loop if conversion is successful
    except ValueError:
        print("Please enter a number for age.")  # error message for invalid input

person = {                               # store details in a dictionary
    "Name": name,                        # save name
    "Hometown": hometown,                # save hometown
    "Age": age                           # save age
}

print(f"{person['Name']}\n{person['Hometown']}\n{person['Age']}")  
# print name, hometown, and age on separate lines

