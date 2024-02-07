# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

# Solution:
# I have developed a program that checks if an integer is power of two.
# There is a function I created called is_power_of_two to perform this check.
# First, within the function, I verify the input and return False if it is less than or equal to zero because then it cannot be a power of two.
# Then, until we run out of even numbers, use while loop that divides 2 into the input number.
# If the final result after division by 2 is one, it means the given integer was indeed a power of two; otherwise, not.
# Additionally, I’ve included input validation so as to ensure that a valid integer value is entered by the user.
# Whereby if the input doesn’t validate then i propose a random instance of a valid integer for guidance
# Finally, I allow the user to make multiple attempts (up to 5) to enter a valid integer.


import random # Import the random module to generate random numbers

# Define a function to check if an integer is a power of two
def is_power_of_two(n): 
    if n <= 0: # If the input is less than or equal to 0, it cannot be a power of two
        return False # Return False
    while n % 2 == 0: # While the input is divisible by 2
        n = n // 2 # Divide the input by 2 using integer division
    return n == 1 # Return True if the final result is 1, otherwise return False

attempts = 5 # Set the maximum number of attempts to 5
for _ in range(attempts): # Loop for the maximum number of attempts
    user_input = input("Please enter an integer: ") # Prompt the user for input
    try:
        num = int(user_input) # Convert the input to an integer
    except ValueError: # If the input is not a valid integer
        print("Invalid input! Please enter a valid integer.") # Inform the user if the input is not a valid integer
        if attempts > 1: # Check if there are remaining attempts
            print("You have", attempts - 1, "attempts remaining.") # Notify the user of the remaining attempts
        print("For example:", random.randint(1, 100)) # Provide a random example of a valid integer
        attempts -= 1 # Decrease the number of remaining attempts by 1
        continue # Skip to the next iteration of the loop
    else: # If the input is a valid integer
        if is_power_of_two(num): # Check if the input is a power of two by calling the function
            print("True") # Print True if the input is a power of two
        else:
            print("False") # Print False if the input is not a power of two
        break # Exit the loop if a valid input is provided

if attempts == 0: # If all attempts are used and no valid input is provided
    print("No valid input provided. Here's a random example:", random.randint(1, 100)) # Provide a random example of a valid integer

# Possible Outputs:
# 1. If the user enters 8:
#    Output: True
# 2. If the user enters 6:
#    Output: False
# 3. If the user enters a non-integer input:
#    Output: (for example)
#            Invalid input! Please enter a valid integer.
#            For example: 73
# 4. If the user fails to enter a valid integer within 5 attempts:
#    Output: (after 5 attempts)
#            You've reached the maximum number of attempts.