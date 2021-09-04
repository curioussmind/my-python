# tuple is a collection of item separated by comma in a parenthesis.
my_tupple = (1, 2, 3) # tuple with three items

empty_tupple = () # empty tuple

#  THE TUPLE BUILT IN
name = "oktavianus"
my_tupple = tuple(name)
print(my_tupple)
print(len(my_tupple)) # print length of tuple
print(my_tupple[1]) # tuple indexing
print(my_tupple[2:4]) # slicing

# tuple are immutable means we can't change the value of an element in the tuple

print("n" in my_tupple) # checking value existence
