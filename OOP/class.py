from typing import Mapping


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."
    

miles = Dog("Miles", 4, "black") # creating object
print(miles)

#sound_woof = miles.speak("Woof Woof") # calling instance method
#print(sound_woof)

#sound_bow = miles.speak("Bow Bow") # calling instance method
#print(sound_bow)

phillo = Dog("Phillo", 5, "brown")
print(f"{phillo.name}'s coat is {phillo.coat_color}.")



