# Encapsulation - data hiding
class Person:
    def __init__(self):
        self.name = "Sanchitha"
        # set age is a private variable
        # we use __ before the variable name
        self.__age = 22

    # if we need access private variable we used getters and setters functions

    # setter function
    def set_age(self, age):
        self.__age = age
    # getter function

    def get_age(self):
        return self.__age

    def sleep(self):
        print("Sleeping", self.name)


# create object using person class
sanchitha = Person()

print(sanchitha.sleep())
# we can not access __age private variable outside the function

# if we need access private variable we used getters and setters functions
# we can access and set private variable using getter and setter like below

# print private variable value using getter function
print("Before update", sanchitha.get_age())
# set new value to private variable using setter function
sanchitha.set_age(23)
print("After update", sanchitha.get_age())


