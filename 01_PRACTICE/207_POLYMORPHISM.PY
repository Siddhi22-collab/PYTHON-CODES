class Dog:
    def sound(self):
        print("dog sound")  
class Labrador(Dog):
    def sound(self):
        print("BHOWWWW") 
class Beagle(Dog):
    def sound(self):
        print("Barks") 
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()  
calc = Calculator()
print(calc.add(66, 100))
print(calc.add(45, 64, 78))  