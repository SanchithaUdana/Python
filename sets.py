# python sets

x = {"hello", "world", "hellow", "1", "2"}

print(x)
x.add("Hellow")  # hash function
print(x)

x.remove("1")
print(x)

y = {"123", "234", "456"}

# add two set
print(x.union(y))  # union operator
print(x | y)  # pipe operator

# subtract sets
# remove the second set elements in first set
# we can find different element between two set
a = {123, 234, 345}
b = {123, 345}

print(a - b)

# check item available in a set

abc = {1, 2, 3, 4, 5}
print(1 in abc)
print(1 not in abc)
