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

