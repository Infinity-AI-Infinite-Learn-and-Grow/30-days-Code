# Concatenate the string 'Thirty', 'Days', 'Of', Code to a single string, 'Thirty Days Of Code'
# Use capitalize(), title(), swapcase() methods to format the value of the string Ai For All
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma

str = " ".join(["Thirty", "Days", "Of", "Code"])
print("Concatenated string: ", str, "\n")

str = "Ai For All"
print("Capitalized string: ", str.capitalize())
print("Titled string:", str.title())
print("Case-swaped string: ", str.swapcase(), "\n")

str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
list = str.split(", ")
print("Split string: ", list, "\n")
