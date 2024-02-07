# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.

# Solution:
# I've crafted a program to count the number of vowels in a sentence provided by the user.
# For this purpose, I designed a function named count_vowels, which takes a string 's' as input.
# Within the function, I initialized a counter variable 'count' to track the number of vowels.
# I defined a string 'vowels' containing all the vowels, both in lowercase and uppercase.
# Next, I iterated through each character in the input string 's' using a loop.
# If the current character was found in the 'vowels' string, I incremented the 'count' variable.
# Ultimately, I returned the 'count' variable, which holds the total count of vowels in the input string.

def count_vowels(s):
    # Define a string of vowels
    vowels = "aeiouAEIOU"
    # Initialize a counter for the number of vowels
    count = 0
    # Loop through each character in the input string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the counter if it's a vowel
            count += 1
    # Return the total count of vowels
    return count

# Prompt the user to enter a sentence
user_input = input("Please enter a sentence: ")

# Check if the user provided a sentence
if user_input.strip(): # If the input is not empty after stripping leading and trailing spaces
    # Call the function to count vowels and print the result
    print("You entered:", user_input)
    print("The Number of vowel(s) are:", count_vowels(user_input))
else:
    print("No sentence provided.") # Inform the user that no sentence was provided

# Example Output:
"""
Please enter a sentence: Hello World
You entered: Hello World
The Number of vowel(s) are: 3
""" 
