# generator
# can use for memory efficiency

def get_odd_number(upper_limit):
    for num in range(0, upper_limit):
        if num % 2 == 1:
            print("Odd", num)  # first print this
            yield num  # this keyword is used to create generator "yield"


print("Start")

x = get_odd_number(10)
for i in x:
    print("loop", i)  # secondary print this

print("End")
