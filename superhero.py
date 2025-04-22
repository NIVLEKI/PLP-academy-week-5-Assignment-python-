# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Encapsulation: underscore means "protected"

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self._age} years old.")

# Inherited class
class Superhero(Person):
    def __init__(self, name, age, power, city):
        super().__init__(name, age)  # Call parent constructor
        self.power = power
        self.city = city

    def use_power(self):
        print(f"{self.name} uses {self.power} to protect {self.city}!")

# Creating superhero objects
hero1 = Superhero("StormBlaze", 30, "Lightning Speed", "Metroville")
hero2 = Superhero("ShadowKnight", 28, "Invisibility", "Gothica")

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
