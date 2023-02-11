#Concatenate the string 'Thirty', 'Days', 'Of', Code to a single string, 'Thirty Days Of Code'.

from posixpath import split


print(" ".join(['Thirty','Day','Of','Code']))

#Use capitalize(), title(), swapcase() methods to format the value of the string Ai For All.

str="artificial Intelligence"
print(str.capitalize())
print(str.title())
print(str.swapcase())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

list="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(list)