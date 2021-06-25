# "infinite" number of arguments:

def call_person(*people):
    # print("this is", people) # if we'll do it like that it will just write them in one line as an array.
    for person in people:
        print("This is", person)


call_person("Ignat", "Nick", "And so on...")  # we can add as many is we like
