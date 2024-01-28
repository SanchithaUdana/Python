# packed arguments

def find_total(*marks):  # we used * mark to define packed argument
    total = 0
    print(type(marks))
    for i in marks:
        total += i
    print("Total is", total)
    print()


print("calling 01")
find_total(12, 45, 56, 54)

print("calling 02")
find_total(12, 45, 56, 54, 46, 53, 23)

print("calling 03")
find_total(12, 45)




