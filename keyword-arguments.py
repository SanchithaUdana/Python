# Keyword Arguments
# named argument values converted to a dictionary
def my_form(**form):  # we used ** to define keyword arguments
    print(form)
    print(type(form))
    print("\"Hello\"", form['name'])


my_form(name="sanchitha", subject="ICT")
