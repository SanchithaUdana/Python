# List Comprehension under any condition
def is_even(number):
    return {number: "Even"} if number % 2 == 0 else {number: "Odd"}


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# return new list consider the condition "if i < 5" and the function "is_even()"
b = [is_even(i) for i in a if i < 5]

print(a)
print(b)
