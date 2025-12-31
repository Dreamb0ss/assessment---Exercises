def check_even(number):
    # checks if the number is even or odd
    if number % 2 == 0:
        return "The number is even"  
        # returned when number is divisible by 2
    else:
        return "The number is odd"  
        # returned when number is not divisible by 2

def main():
    num = int(input("Enter a number: "))  
    # ask user to enter a number
    result = check_even(num)  
    # call function to check even or odd
    print(result)  
    # display the result

if __name__ == "__main__":
    main()  
    # runs main when the program is executed
