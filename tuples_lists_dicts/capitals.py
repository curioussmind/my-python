import random

capital_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Denver',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state, capital = random.choice(list(capital_dict.items()))

while True:
    guess = input(f"What is the capital of '{state}'?").lower()
    if guess == 'exit':
        print(f"The capital of '{state}' is '{capital}'.")
        print("Goodbye")
        break
    elif guess == capital.lower():
        print("Correct! Nice job.")
        break