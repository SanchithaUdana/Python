# Dictionary Data Type

x = {"51100": "aralaganwila", "51104": "diuldamana", "51200": "polonnaruwa", "o": "zero", }

print(x)

print(x.keys())
print(x.values())
print(x["51100"])

y = {1: "one", 2: "two"}

# get element in dictionary, if key not available, we can give special value to display
print(y.get(3, "none"))
print(y.get(1, "none"))

# delete element using key
del y[1]
print(y)

# delete the all dictionary
y.clear()
print(y)

xyz = {
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9, 10],
    "c": 15
}

dList = xyz["a"]  # assign a pointer reference ( pass by reference )
dList.append(956)
print(xyz)


