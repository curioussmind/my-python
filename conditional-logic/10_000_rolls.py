import random

def roll():
    return random.randint(1, 6)

print(roll())
        

# Simulate 10,000 rolls of a die and display the average number rolled.
rolls_num = 10_000
total_rolls = 0

for trial in range(rolls_num):
    total_rolls = total_rolls + roll()

avg_rolls = total_rolls / rolls_num

print(f"The average result of {rolls_num} rolls is {avg_rolls}")