import re


print("Calculator")
print("Type 'quit' to exit\n")

previous = 0.0
run = True


def perform_math():

    global previous
    global run
    equation = ""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    # eval function can't be used if there is a possibility of strange input. So we remove everything with regular expression (regex)
    else:
        equation = re.sub("[a-z A-Z,:()" "]", "", equation)
        if previous == 0:
            try:
                previous = eval(equation)
            except (SyntaxError, ZeroDivisionError):
                pass
        else:
            try:
                previous = eval(str(previous) + equation)
            except (SyntaxError, ZeroDivisionError):
                pass


while run:
    perform_math()
