# slicing in python is very important

x = ["a", "b", "c", "d"]

print(x[0:4])  # 0 to 4 include 0, 1, 2, 3  output ['a', 'b', 'c', 'd']
print(x[:4])  # 0 to 4 include 0, 1, 2, 3  output ['a', 'b', 'c', 'd']
print(x[0:])  # 0 to 4 include 0, 1, 2, 3  output ['a', 'b', 'c', 'd']

print(x[1:-1])  # output ['b', 'c']
print(x[:-1])  # output ['a', 'b', 'c']

# length
print(len(x))  # output 4
