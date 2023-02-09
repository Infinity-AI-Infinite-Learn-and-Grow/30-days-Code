"""Day 5: In the GitHub repository, Infinity-AI(Infinite Learn and Grow)/30-days-code inside the Day-5 folder create your_name.py file as defined in the readme.md file.
Declare IT_Company list with more than 5 values.
Print the first, middle, and last company
Insert it company name at a second position and last position.
Reverse the list in descending order using the reverse() method
Remove the last IT company from the list
Destroy the IT company's list"""


IT_Company=['apple','google','microsoft','amazon','samsung']
print(IT_Company)


print(f"first: {IT_Company[0]} \nmiddle: {IT_Company[2]} \nlast company: {IT_Company[-1]}")

print(IT_Company.pop(-1))
print(IT_Company)

#destroy
del IT_Company

