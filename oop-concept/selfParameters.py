# class name is must be start using capital letter
class Dog:
    # class body
    name = "Unknown"

    def setName(self, name):
        self.name = name

    # self argument is automatically passed by python
    # we can class parameters using self keyword
    # self is the represent the own class
    def welcome(self):
        # print the message using f string method with class parameters
        msg = f"Hello Baw Baw {self.name}"
        print(msg)


# object

dog1 = Dog()
dog1.setName("Scooby")
dog1.welcome()




