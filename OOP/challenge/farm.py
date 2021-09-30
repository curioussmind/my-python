class Animal:

    def __init__(self, name, total):
        self.name = name
        self.total = total
    
    # animal informaqtion 
   #  def __str__(self):
        #pass # to print animal informations
    def __str__(self):
        if self.total > 1:
            return f"There are {self.total} {self.name.capitalize()}s in this farm."
        else:
            return f"There are {self.total} {self.name.capitalize()} in this farm."

    def total (self, total):
        return total
    
    def speak(self, sound):
        return f"This animal sound like this: '{sound}'"
    
    def legs_number(self, legs):
        return legs
    
    def they_eat(self, food):
        return food


class Mammals(Animal):
    def legs_number(self, legs=4):
        return legs
    
    def total(self, total):
        return total

class Poultry(Animal):
    def legs_number(self, legs):
        return legs
    
    def total(self, total):
        return total

class Insects(Animal):
    def legs_number(self, legs):
        return legs
    
    def total(self, total):
        return total


cow = Mammals('cow', 30)
print(cow)

chicken = Poultry('chicken', 500)
print(chicken)

