x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

file = open("join-data", "w")

y = [str(i) for i in x]  # comprehension list

# join method for joining data with special character
# that only use in iterable
# ",".join()
file.write(",".join(y))

