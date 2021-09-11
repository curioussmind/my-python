# hold information in pairs of data called key-value pairs. 

# creating dictionariy
capitals = {
    "California": "Sacramento", #each key and value separated by colon (:)
    "New York": "Albany", # each items or key and value pairs separated by comma
    "Texas": "Austin", # enclosed by curly braces
}

print(capitals)
print(type(capitals))

# using dict() built in function
key_value = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin"),
)

cities = dict(key_value)
print(cities)

# initialize emoty dicts
empty_dict = {}
empty_dict2 = dict()
print(f"the type of empty_dict is {type(empty_dict)}")
print(f"the type of empty_dict2 is {type(empty_dict2)}")