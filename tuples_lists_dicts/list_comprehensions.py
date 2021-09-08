# list comprehension is another way to create a list from an existing iterable
numbers = (1, 2, 3, 4, 5)
squares = [num ** 2 for num in numbers] # list comprehensions
print(squares)

# using traditional for loop
square = [] # initialize an empty list
for n in numbers:
    square.append(n ** 2)
print(square)

# LIST COMPREHENSIONS ARE COMMONLY USED TO CONVERT VALUES IN ONE LIST TO A DIFFERENT TYPE
str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(v) for v in str_numbers]
print(float_numbers)