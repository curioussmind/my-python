# A loop is a block of code that gets repeated over and over again either a specified number of times or until some condition is met.
# There are two kinds of loops in python: while loops and for loops

# WHILE loops --> repeat a section of code while some condition is true.

# determines if it is true or false. If the test condition is true, then the code in the loop body is executed. Otherwise, the code in the body is skipped and the rest of the program is executed.
n = 1 # initialize variable
while n < 5: #while statement followed by condition (n < 5)
    print(n)
    n = n + 1

# One use of a while loop is to check whether or not user input meets some condition and, if not, repeatedly ask the user for new input until valid input is received.

# For instance, the following program continuously asks a user for a positive number until a positive number is entered:

num = float(input("Enter a positive number: "))

while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))

# one line while loops
print("one line while loops:")
n = 5
while n > 0: n -= 1; print(n)