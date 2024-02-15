#  inheritance
class Animal:  # parent class
    def __init__(self, breed):
        self.breed = breed

    def talk(self):
        print("Animal is talking...")

    def walk(self):
        print("Animal is walking...")


class Dog(Animal):  # child class inherit from Animal Class
    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("breed Dog")
        self.name = name
        print("Dog is created")

    # Method Overriding
    # redefined the parent class method in child class
    def talk(self):
        print("Dog is talking...")
        # and we can call parent talk method also
        super(Dog, self).talk()


dog1 = Dog()

dog1.talk()
