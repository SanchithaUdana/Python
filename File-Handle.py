file = open("data.txt")

# content = file.read()
# print(content)

for i, line in enumerate(file):
    print(f"line {i}", line)

file.close()




