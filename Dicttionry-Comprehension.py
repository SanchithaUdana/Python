# Dictionary Comprehension under any condition
def is_even(number):
    return "even" if number % 2 == 0 else "Odd"


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# return new dictionary consider the condition "if i < 5" and the function "is_even()"
b = {i: is_even(i) for i in a if i < 5}

print("Given List :", a)
print("Created Dictionary :", b)

