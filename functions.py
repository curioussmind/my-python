# FUNCTIONS ARE VALUE and can be assigned to variable
# HOW PYTHON EXECUTES FUNCTION:
    # 1 the function is CALLED and any arguments are passed to the function as input
    # 2 The function executes and some actions are performed with the arguments
    # 3 The function returns and the original function call is replaces with return value.

num_letters = len("four")
print(num_letters)

# FUNCTIONS CAN HAVE SIDE EFFECTS
# --> when a function changes or affects something external
# example print()
# When you call print() with a string argument, the string is displayed in the Python shell as text. But print() doesn’t return any text as a value.
# To see what print() returns, you can assign the return value of print() to a variable:
return_value = print("What do I return?") # --> what do I return?
return_value # --> print nothing
