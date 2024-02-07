file = open("data.txt",  )

# content = file.read()
# print(content)

for i, line in enumerate(file):
    print(f"line {i} ->", line)

file.close()

file2 = open("data.txt", "w")  # file reading mode W - write

# add data to text file

for i in range(0, 20):
    file2.write(str(i) + "\n")

file2.close()



