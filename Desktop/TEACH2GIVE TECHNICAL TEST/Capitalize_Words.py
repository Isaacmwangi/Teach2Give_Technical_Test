# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.

# Solution:
# I've coded up a program that capitalizes the first letter of every word in a given string.
# It does this by defining capitalize_words() function with its parameter as 's' which is meant to be a string.
# When inside the function we split the input line into individual words by using the split() method.
# Therefore, I created an empty string called ‘result’ where I would store my final changed sentence.
# Since words are lined up in the list format, then it was necessary for me to use a loop that accessed each word at a go before proceeding to the next one.
# For each word, I capitalized the first letter using the upper() method and concatenated it with the rest of the word.
# In order to achieve my desired output, at last, I had to combine all modified words so that they formed one string separated by space character. 
# Then this function removes all trailing spaces from ‘result’ before returning it.


def capitalize_words(s):
    # Split the input string into a list of words
    words = s.split()
    # Initialize an empty string for the result
    result = ""
    # Loop through each word in the list
    for word in words:
        # Capitalize the first letter of the word and append it to the result with a space
        result += word[0].upper() + word[1:] + " "
    # Return the result without trailing spaces
    return result.strip()

# Prompt the user to enter a string
user_input = input("Please enter a Sentence: ")

# Check if the user provided a string
if user_input.strip(): # If the input is not empty after stripping leading and trailing spaces
    # Call the function to capitalize words and print the result
    print("Original string:", user_input)
    print("Capitalized string:", capitalize_words(user_input))
else:
    print("No string provided.") # Inform the user that no string was provided

# Example Output:
"""
Please enter a string: i love programming
Original string: i love programming
Capitalized string: I Love Programming
""" 
