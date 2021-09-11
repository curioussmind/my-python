# create a dictionary that maps each state name to a dictionary containing the capital city
# and the state flower.

states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
    },
    "New York": {
        "capital": "Albany",
        'flower': "Rose"
    },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
    },
}
# The value of each key is a dictionary
print(states["Texas"])
print(states["California"]["flower"])

# We'll use the dictionaries very often 
