# just like list and tuple, dictionaries are iterable

capitals = {
    "California": "Sacramento", #each key and value separated by colon (:)
    "New York": "Albany", # each items or key and value pairs separated by comma
    "Texas": "Austin", # enclosed by curly braces
}

for key in capitals:
    print(key)

# we do this if we want to access key and value in a dict
for state in capitals:
    print(f"The capital of {state} is {capitals[state]}")

# we can use .items() method to print the tuple of states with their corresponding values
print(capitals.items())

# WE CAN USE .items() to loop over a dictionary keys and values simultaneously
for state, capitals in capitals.items():
    print(f"The capital of {state} is {capitals}")

# When you loop over capitals.items(), each iteration of the loop produces
# a tuple containing the state name and the corresponding capital
# city name. By assigning this tuple to state, capital, the components
# of the tuple are unpacked into the two variable state and capital

# list of data types that are va;id for dictionary keys
    # ~ integers
    # ~ floats
    # ~ strings
    # ~ booleans
    # ~ tuples

