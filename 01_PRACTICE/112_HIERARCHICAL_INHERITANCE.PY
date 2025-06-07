# Base class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Derived class 1
class Dog(Animal):
    def speak(self):
        print("The dog barks")

# Derived class 2
class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Derived class 3
class Cow(Animal):
    def speak(self):
        print("The cow moos")

# Creating objects of each derived class
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the speak method
dog.speak()   # Output: The dog barks
cat.speak()   # Output: The cat meows
cow.speak()   # Output: The cow moos
