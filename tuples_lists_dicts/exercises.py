# PART 1
food = ["rice", "beans"] # 1
food.append("broccoli") # 2
food.extend(["bread", "pizza"]) # 3
print(food[:2]) # 4
print(food[-1]) # 5

# PART 2
breakfast = "eggs, fruit, orange juice".split(",") # 6
print(breakfast)
print(len(breakfast)) # 7

lengths = [len(string) for string in breakfast] # 8 
print(lengths)

