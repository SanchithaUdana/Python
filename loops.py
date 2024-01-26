# for loop

x = [1, 2, 3, 4, 5]

for item in x:
    print(item)

print()

for j in range(5):
    print("Hello World!")

print()

for i in range(1, 10, 2):
    print(i)

print()

# enumerate function

for item in enumerate(x):
    index = item[0]  # item is a tuple. because enumerate method return a tuple
    value = item[1]
    print("index", index, "--> Value is", value)

print()

#  we can pass variable to assign the tuple values

for index, value in enumerate(x):
    print("index", index, "--> Value is", value)

# while loop

count = 0

while count < 10:
    print("count", count, end="#")
    print()
    count += 1


# break and continue keywords

number = 0

while True:
    print(number)
    if number >= 10:
        break  # break keyword
    number += 1

for s in range(1, 10):
    if s == 5:
        continue
    print(s)




