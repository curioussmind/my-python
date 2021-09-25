class Animal:

    def __init__(self, animal_name, animal_numbers, animal_categories, product):
        self.animal_name = animal_name
        self.animal_numbers = animal_numbers
        self.animal_categories = animal_categories
        self.product = product

    
    # animal informaqtion 
    def __str__(self):
        pass # to print animal informations

    def __speak__(self, sound):
        return f"This animal sound like this: '{sound}'"

def 