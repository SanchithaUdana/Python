# list
x = [12, 13, 14, 15]
print(x)

# python is Zero Index programing language

print(x[0])
print(x[3])

# index update
x[0] = 100
print(x)

# add item end of the list
x.append(243)
print(x)

# add item specific index
x.insert(1, 500)
print(x)

# remove item using item value
x.remove(500)
print(x)

# remove item using index
x.pop(0)
print(x)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(list1 + list2)

check1 = 2 in list1
print(check1)

check2 = "Yes" if (2 in list1) else "No"
print(check2)

check3 = 2 not in list1
print(check3)



