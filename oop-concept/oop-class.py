# class name is must be start using capital letter
class Dog:
    # class body
    name = ""

    def bark(self):  # self argument is automatically passed by python
        print("baw baw")


# object

dog1 = Dog()
dog1.name = "scooby"
dog1.bark()

# call function using class name
# must pass the object name
Dog.bark(dog1)

