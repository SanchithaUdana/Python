class Person:
    # this is a class attribute
    # using class attributes, we can access that attributes via the class name
    types = ['teacher', 'student', 'assistant']

    def __init__(self):
        self.name = "Sanchitha"
        self.__age = 22
        self._city = "Polonnaruwa"

    # this is instant methods
    def print_info(self):
        print("Name: " + self.name)

    # this is a class method
    @classmethod
    def get_types(cls):
        return cls.types

    # this is static method
    # we not pass self or cls into static methods
    @staticmethod
    def cal_age(today, dob):
        return today - dob


# --------------------------------------------------

# access class attributes using class name
# not need to create an instant to access class attributes,
# but we can access using instant
# we can not access object functions and data via class - cls
# cls is the standard for represent class in class methods

sanchitha = Person()

print(Person.types)
print(Person.get_types())

# we can access static method using instant and class
a = sanchitha.cal_age(2023, 2002)
b = Person.cal_age(2023, 2002)

print(a)
print(b)

