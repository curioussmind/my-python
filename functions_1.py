# ANATOMY OF A FUNCTION
def multiply(x, y):     # function signature
    product = x * y     # function body
    return product      # function body

# CALLING USER-DEFINED FUNCTION
# You call a user-defined function just like any other function. Type the function name followed by a list of arguments in 
# between parentheses.
# For instance, to call multiply() with the argument 2 and 4, just type:
multiply(2, 4)

# FUNCTION WITJ NO RETURN STATEMENT
# All functions in Python return a value, even if that value is None. How- ever, not all functions need a return statement.
# For example, the following function is perfectly valid:
def greet(name):
    print(f"Hello, {name}!")

greet("Dave") # function calling
