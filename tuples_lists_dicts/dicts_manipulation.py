# first thing to remember is that dictionaries are mutable

capitals = {
    "California": "Sacramento", #each key and value separated by colon (:)
    "New York": "Albany", # each items or key and value pairs separated by comma
    "Texas": "Austin", # enclosed by curly braces
}

print(capitals["Texas"]) # items in dictionary are accessed by key

# adding and removing value
#            key         value
capitals["Colorado"] = "Denver" # add Colorado to our dictionary
print(capitals)

#each key in a dictionary can only be assigned a single value, if a key is given a new value python will overwrite the old one

# remove item from dictionary
del capitals["Texas"]
print(capitals)

# checking the existence of dictionary keys
# KeyError will arise if we try to access a key doesn't exist in a dictionary
print("Arizona" in capitals)
print("California" in capitals)

if "Arizona" in capitals:
    print(f"The capital of Arizona is {capitals['Arizona']}.")
else:
    print("Sorry Arizona does not exist in our database :(.")


