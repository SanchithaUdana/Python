# String Formatting
# have 4 types
#   01. String Concatenation
#   02. C string formatting
#   03. .format() string formatting
#   04. f formatting


name = "Sanchitha"
height = 170.34

# normal string formatting - string concatenation
message1 = "Hello " + name + ", your Height is " + str(height)
print(message1)

# C string formatting
message2 = "Hello %s, Your height is %.2f" % (name, height)
print(message2)

# format function string formatting
message3 = "Hello {0}, your height is {1}".format(name, height)
print(message3)

# f string formatting
message4 = f"Hello {name}, your height is {height}"
print(message4)

