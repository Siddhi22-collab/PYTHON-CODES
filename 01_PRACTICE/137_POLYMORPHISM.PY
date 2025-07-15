class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

# Polymorphism
for animal in (Cat(), Cow()):
    animal.sound()
