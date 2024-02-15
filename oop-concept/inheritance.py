#  inheritance
class Animal:
    def __init__(self, breed):
        self.breed = breed

    def talk(self):
        print("Animal is talking...")

    def walk(self):
        print("Animal is walking...")


class Dog(Animal):
    def __init__(self, name="Unknown"):
        super().__init__("breed Dog")
        self.name = name
        print("Dog is created")


dog1 = Dog()

dog1.talk()
