

# default arguments will be printed if we will not pass them in function later on when we will be calling it
def print_something(name="Someone", age="Unknown"):  # <-- default arguments
    # if we will concatenate here with "+" sign then with number entered in argument later it won't work. the we will have to wrap it into a str() finction
    print("My name is", name, "and my age is", age)


print_something()
print_something("Ignat", 27)
print()
# to pass arguments in different order we have to use key word first.There is no other way to bypass the order of the arguments in which they are give in function.
print_something(27, "Ignat")
print_something(age=27, name="Ignat")
