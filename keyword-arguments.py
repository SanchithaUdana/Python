# Keyword Arguments
def my_form(**form):
    print(form)
    print(type(form))
    print("\"Hello\"", form['name'])


my_form(name="sanchitha", subject="ICT")
