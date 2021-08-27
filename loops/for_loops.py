# FOR loop
# A for loop executes a section of code once for each item in a collection of items. The number of times that the code is executed is determined by the number of items in the collection.

for letter in "python":
    print(letter)

# The following program asks the user to input an amount and then displays how to split that amount between 2, 3, 4, and 5 people:
amount = float(input("Enter an amount: "))

for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each.")

# for loops are generally used more often than while loops in Python. Most of the time, a for loop is more concise and easier to read than an equivalent while loop.
