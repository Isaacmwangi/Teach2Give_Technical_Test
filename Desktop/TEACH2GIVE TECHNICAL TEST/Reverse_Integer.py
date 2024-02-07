# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit ordering.
# Examples:
# For input 500, the program should return 5. For input -56, the program should return -65. For input -90, the program should return -9. For input 91, the program should return 19.
# Solution:
# For input 500, the program should return 5. For input -56, the program should return -65. For input -90, the program should return -9. For input 91, the program should return 19.
# Solution:
# I've created a program that will allow the user to reverse the digits of the entered integer.
# The program initially requests for an integer from the user and then verifies the said input.
# It keeps asking for user inputs until a valid integer or maximum number of trials are reached.
# Once a valid integer is provided, the program reverses the digits of the integer and returns the result.
# Also, I have handled negative integers correctly so that their signs remain intact.


# Maximum number of attempts
max_attempts = 5
attempts = 0

# Function to reverse the digits of an integer
def reverse_integer(n):
    sign = -1 if n < 0 else 1 
    # Determine the sign of the integer
    reversed_num = int(str(abs(n))[::-1]) 
    # Reverse the absolute value of the integer and convert it back to an integer
    return sign * reversed_num 
    # Multiply by the original sign to maintain sign of the integer

# Repeat until a valid integer is provided or maximum attempts reached
while attempts < max_attempts:
    user_input = input("Please enter an integer: ")
    try:
        num = int(user_input)
        # Convert the input to an integer
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        attempts += 1
        continue
    else:
        # Reverse the digits of the integer using the reverse_integer function
        reversed_num = reverse_integer(num)
        print("Reversed integer:", reversed_num)
        break

    attempts += 1

# Inform the user if maximum attempts are reached
if attempts == max_attempts:
    print("Sorry, maximum attempts reached. Please try again later.")

# Possible Outputs:
# If the user enters 500:
# Output: Reversed integer: 5
# If the user enters -56:
# Output: Reversed integer: -65
# If the user enters -90:
# Output: Reversed integer: -9
# If the user enters 91:
# Output: Reversed integer: 19
# If the user enters "abc" (invalid input):
# Output: Invalid input! Please enter a valid integer.
# If the user exceeds maximum attempts without providing a valid integer:
# Output: Maximum attempts reached. Please try again later.
