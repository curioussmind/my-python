class Animal:

    def __init__(self, name, total):
        self.name = name
        self.total = total
    
    # animal informaqtion 
   #  def __str__(self):
        #pass # to print animal informations
    def __str__(self):
        return f"There are {self.total} {self.name} in this farm."
    
    def total (self, total):
        if total > 1:
            self.name = self.name + 's'
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
    
    def total(self, total=20):
        return total

cow = Mammals('cow', 20)

print(cow)