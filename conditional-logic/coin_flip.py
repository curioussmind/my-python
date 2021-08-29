import random

# create a definiton to flip the coin. 0 for tails and 1 for head
def coin_flip(): 
    if random.randint(0, 1) == 0:
        return "tails"
    else:
        return "heads"


flips = 0 # start flip from 0
trials_num = 10_000

for trial in range(trials_num):
    if coin_flip() == "heads":
        flips = flips + 1 #increment the number of flips by one
        while coin_flip() == "heads":
            flips = flips + 1
        flips = flips = 1
    else:
        flips = flips + 1
        while coin_flip() == "tails":
            flips = flips + 1
        flips = flips + 1


avg_flips_per_trial = flips /trials_num
print(f"The average number of flips per trial is {avg_flips_per_trial}.")