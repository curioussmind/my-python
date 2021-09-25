# Dog class

class Dog(object):
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

# CREATE THREE CHILD CLASSES FROM THE ABOVE CLASS or IN OTHER WORDS INHERITING FROM ABOVE CLASS
class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"): # override the instance method from parent class, set the default sound with "Arf"
        return f"{self.name} says {sound}."

class Daschshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRusselTerrier("Miles", 4)
buddy = Daschshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles)
print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("woof"))
print(type(jack)) # check which class this obj belonngs to
print(isinstance(miles, Dog)) # check if miles is an instance of Dog class

# referring ti class JackRusselTerrier(Dog) on line 17
yoko = JackRusselTerrier("Yoko", 4)
print(yoko.speak()) # autommatically sound arf based on the JackRusselTerrier(Dog) chuld class :