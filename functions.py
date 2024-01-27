# functions in python

#  create function including parameters
# mark is a positional parameter
# subject is a default arguments
#  we can not pass parameters after the default parameter
def get_grade(mark, subject="Unknown"):
    if 0 <= mark < 35:
        print("W", subject)
    elif 35 <= mark < 55:
        print("S", subject)
    elif 55 <= mark < 65:
        print("C", subject)
    elif 65 <= mark < 75:
        print("B", subject)
    elif 75 <= mark <= 100:
        print("A", subject)
    else:
        print("Invalid Mark")


# call the function

marks_List = [12, 23, 45, 67, 54, 56, 76, 78]

for i in marks_List:
    get_grade(i)

# Named argument
# if we pass named argument we can pass named argument after the positional arguments
# passed in the calling the function

get_grade(subject="sinhala", mark=78)
