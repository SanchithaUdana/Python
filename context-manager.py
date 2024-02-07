#  we used "with" keyword to manage contexts

with open("data.txt", "w") as file:
    li = [str(i) for i in range(0, 20)]
    data = ','.join(li)
    file.write(data)
