#  inheritance
class Animal:  # parent class
    def __init__(self, breed):
        self.breed = breed

    def talk(self):
        print("Animal is talking...")

    def walk(self):
        print("Animal is walking...")


class Mammal:
    def __init__(self):
        print("i am mammal")

    def feed(self):
        print("feeding milk...")


class Dog(Animal, Mammal):  # child class inherit from Animal Class
    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("breed Dog")
        self.name = name
        print("Dog is created")


dog1 = Dog()

dog1.talk()
# call from Mammal class
dog1.feed()

