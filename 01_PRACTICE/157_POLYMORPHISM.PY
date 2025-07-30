class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly high")

b = Bird()
s = Sparrow()

b.fly()
s.fly()
