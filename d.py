import re  # importing regex(regular expression) library

string = "'I AM NOT YELLING', she said. Though we all knew it was not true."

# first parameter we enter is what we want to change in this case all CAPITAL letters from A to Z with an empty string so that only 'spaces' left.
# Same we can do for lower case letters.
new_string = re.sub("[A-Z]", "", string)

print(new_string)
print()
new_string = re.sub("[.,']", "", string)  # punctuations removed
print(new_string)
print()
# removed all lowercase letters and with plus sign and quotes with space (+" ") removed spaces
new_string = re.sub("[a-z + " "]", "", string)
print(new_string)
