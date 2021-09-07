# indexing and slicing work alomst the same as tuple

alphabet = ['a', 'b', 'c', 'd']
alphabet[1] # accessing item at index 1
new_alphabet = alphabet[1:3] # creating list from existing list by slicing 

'z' in new_alphabet # checking element in the list

# LIST ARE ITERABLE, WE CAN USE FOR LOOP TO ITERATE OVER THEM
for alph in alphabet:
    print(alph * 2)

# CHANGING ELEMENT IN LIST
colors = ["red", "yellow", "green", "blue"]
colors[0] = "burgundy" 
colors # >> ["burgundy", "yellow", "green", "blue"]

# LIST METHOD FOR ADDING AND REMOVING ELEMENT
# insert() used to add a single value into a list. It takes two parameters, the index and the value
colors.insert(1, "orange") 
# if the value for index parameter .insert() is larger than the greatest index in the list, 
# the value will be inserted at the end.
colors.insert(20, 'violet')
colors.insert(-1, "indigo") # we can also use negative indices

# REMOVE ELEMENT OF AT A SPECIFIC INDEX
colors = colors.pop(3) # remove the value from index 3
# colors.pop(-1) # this also works

colors.append("purple") # add new element at the end of a list

colors.insert(len(colors), "black") # insert black at the end of a list

# add several items/ elements to a list
colors.extend(['white', 'maroon'])
print(colors)
