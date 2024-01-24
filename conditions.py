#  if Conditional Statements

age = 12

if age >= 18:
    print("You are Selected")
else:
    print("You are Not Selected")

# Nested if Condition

mark = 54

if 0 <= mark < 35:
    print("W")
elif 35 <= mark < 55:
    print("S")
elif 55 <= mark < 65:
    print("C")
elif 65 <= mark < 75:
    print("B")
elif 75 <= mark <= 100:
    print("A")
else:
    print("Invalid Mark")


#  ternary operator

height = 156
job = "Your Job is " + ("Security" if height > 150 else "labor")
print(job)

experience = 3
post = "Senior" if experience > 2 else "Associate"
print("Your Post is " + post)


