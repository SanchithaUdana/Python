a = [12, 23, 45, 55, 56]
b = []

for i in a:
    b.append(i)

# list comprehension
# that used to create another data structure from one data structure in easily

b = [i for i in a]

b.append(100)

print(a)
print(b)

# The return value is a new list, after checking some condition.
# new-list = [expression for item in iterable if condition == True]
