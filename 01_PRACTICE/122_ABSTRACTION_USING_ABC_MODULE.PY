from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass  # Abstract method, must be implemented by subclass

    def breathe(self):
        print("All animals breathe")

# Concrete class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Object creation
dog = Dog()
dog.sound()      # Output: Dog barks
dog.breathe()    # Output: All animals breathe

cat = Cat()
cat.sound()      # Output: Cat meows
cat.breathe()    # Output: All animals breathe
