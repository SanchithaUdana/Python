# tuples in python

x = (1, "sanchitha", "ict")

print(type(x))

print(x[0])

# tuple expanding

index, name, dep = x

print("Index \t: ", index)
print("Name \t: ", name)
print("Dep \t: ", dep)

# use count how many times given element available
print(x.count("sanchitha"))

# give element index
print(x.index("sanchitha"))



