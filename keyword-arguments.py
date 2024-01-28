# Keyword Arguments
# named argument values converted to a dictionary
def my_form(**formD):  # we used ** to define keyword arguments
    print(formD)
    print(type(formD))
    print("\"Hello\"", formD['name'])


my_form(name="sanchitha", subject="ICT")
# in this function, named parameters are converted into dictionary


def form(name, age):
    print(name)
    print(age)


details = {
    "name": "Sanchitha",
    "age": 45
}

form(**details)
# in this function, dictionary is converted into named parameters
