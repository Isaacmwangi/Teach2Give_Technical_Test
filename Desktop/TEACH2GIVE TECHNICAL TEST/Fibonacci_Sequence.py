# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

# Solutwritten a program to generate the Fibonacci sequence up to 100.
# I have written a program that generates Fibonacci sequence up to 100.
# An example of the fibonacci sequence starts with zero plus one and from there on each new term of the series comes through summing up two terms which are before it.
# In this piece of code; I used variable ‘a’ and ‘b’ as placeholders for first two terms in the series.
# Afterwards using while loop will keep generating Fibonacci numbers until current term surpasses one hundred.
# At every iteration within the loop I print out current term while updating ‘a’ and ‘b’ besides computing next terms via simultaneous assignment statement.

print("The Fibonacci sequence up to 100 is as follows:")
a, b = 0, 1 # initialize the first two terms of the Fibonacci sequence
while a <= 100: # loop until the current term exceeds 100
    print(a) # print the current term
    a, b = b, a + b # calculate the next term using simultaneous assignment

# Possible Outputs:
"""
The Fibonacci sequence up to 100 is as follows:
0
1
1
2
3
5
8
13
21
34
55
89
"""
