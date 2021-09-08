# list have sort method to sort all items in ascending orders
colors = ["red", "yellow", "green", "blue"]
colors.sort()
print(colors)

# sorted numeric items
numbers = [1, 10, 5, 3, 2]
numbers.sort()
print(numbers)

my_friend_name = ["dardi", "abot", "jujus", "hendro"]
my_friend_name.sort(key=len) # sort the items based on the length of each element
print(my_friend_name)

# we can also pass user defined function to key
def get_second_element(item):
    return item[1]

items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_element) # keep in mind that function we pass to key must accept only single arg
print(items)
