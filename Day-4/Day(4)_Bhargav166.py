# - Concatenate the string 'Thirty', 'Days', 'Of', 'Code' to a single string, 'Thirty Days Of Code'.
# - Use capitalize(), title(), swapcase() methods to format the value of the string Ai For All.
# - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

str1 = "Thirty"
str2 = "Days"
str3 = "Of"
str4 = "Code"

str = " ".join([str1, str2, str3, str4])
print("Concatenated string:\t", str, "\n")

str = "Ai For All"
print("Capitalized string:\t", str.capitalize())
print("Titled string:\t\t", str.title())
print("Case-swaped string:\t", str.swapcase(), "\n")

str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
list = str.split(", ")
print("Split string:\t\t", list)
