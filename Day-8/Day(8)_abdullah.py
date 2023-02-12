# Day 8: In the GitHub repository, Infinity-AI(Infinite Learn and Grow)/30-days-code inside the Day-8 folder create your_name.py file as defined in the readme.md file.

# Create a student dictionary and add first_name, last_name,
# gender, age, marital status, skills, country, city, and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using the items() method


# Create a student dictionary and add first_name, last_name,
# gender, age, marital status, skills, country, city, and address as keys for the dictionary
student_dict = {
    "first_name": "Abdullah",
    "last_name": "Shahid",
    "gender": "Male",
    "age": 21,
    "marital_status": "single",
    "skills": "Python",
    "Country": "India",
    "City": "New Delhi",
    "Address": "South Delhi Delhi"
}

# Get the length of the student dictionary
length = len(student_dict)
print(length)

# Get the value of skills and check the data type, it should be a list
print(student_dict.get("skills"))
print(type(student_dict))
# The values in dictionary items can be of any data type

# Modify the skills values by adding one or two skills
student_dict["skills"] = "python", "numpy", "tensorflow",
print(student_dict.get("skills"))

# Get the dictionary values as a list
print(list(student_dict.values()))
print("\n")

# Change the dictionary to a list of tuples using the items() method
print(list(student_dict.items()))
