# class name is must be start using capital letter
class Dog:
    # constructor overriding
    def __init__(self, name="Unknown"):  # set default value for not passed parameter
        self.name = name

    def setName(self, name):
        self.name = name

    def welcome(self):

        msg = f"Hello Baw Baw {self.name}"
        print(msg)


# object

dog1 = Dog("scooby")
dog1.welcome()

dog2 = Dog()
dog2.welcome()




