password = 12345        # correct password
attempts = 5            # number of allowed attempts

while attempts > 0:     # loop while attempts remain
    guess = int(input("Enter password: "))  
    # ask user to enter the password

    if guess == password:
        print("Access granted")  
        # correct password message
        break
    else:
        attempts -= 1  
        # reduce attempts after wrong guess
        print(f"Wrong password. Attempts left: {attempts}")  
        # show remaining attempts

if attempts == 0:
    print("Authorities have been alerted!")  
    # message shown when all attempts are used
