# Odd or even checker
# asks user for number
number = int(input("Enter a whole number: "))

# checks if the number is even or odd by looking at its remainder
if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# spacer for next code
print()

# Password Gatekeeper
# asks user for their password
password = input("Input your password: ")
# gets the amount of letters in the password
length = len(password)

# checks the length of the password
if length < 8:
    print("Password is too short.")
else:     
    print("Password is long enough.")

    
    

