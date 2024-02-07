# Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print "FizzBuzz".

# Solution:
# For a solution of FizzBuzz problem, I use for loop to iterate over numbers from 1 to 100.
# Then for each digit, I start by searching if it is both divisible by five and three. The output in this case is “FizzBuzz”.
# On the other hand, if it is only divisible by three, the answer is “Fizz”.
# Or else, when the number is divisible only by five I will print “Buzz”.
# Lastly, if all those conditions above aren’t satisfied at runtime, then the program will just do a simple printing of that number.

print("Below are the numbers from 1 to 100, with FizzBuzz rules applied:")

for num in range(1, 101): # iterate over numbers from 1 to 100
    if num % 3 == 0 and num % 5 == 0: # check if the number is a multiple of both 3 and 5
        print("FizzBuzz") # print "FizzBuzz" if true
    elif num % 3 == 0: # check if the number is a multiple of 3
        print("Fizz") # print "Fizz" if true
    elif num % 5 == 0: # check if the number is a multiple of 5
        print("Buzz") # print "Buzz" if true
    else:
        print(num) # print the number if none of the above conditions are met

# Possible output:
"""
Below are the numbers from 1 to 100, with FizzBuzz rules applied:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
...
98
Fizz
Buzz
"""
