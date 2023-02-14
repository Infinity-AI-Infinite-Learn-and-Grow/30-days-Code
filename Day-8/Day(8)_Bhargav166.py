# - Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
# - Get the length of the student dictionary
# - Get the value of skills and check the data type, it should be a list
# - Modify the skills values by adding one or two skills
# - Get the dictionary values as a list
# - Change the dictionary to a list of tuples using the items() method

student = {
    'first_name': 'Bhargav',
    'last_name': 'Solanki',
    'gender': 'male',
    'age': '19',
    'marital_status': 'Unmarried',
    'skills': ['Python', 'Java', 'C++'],
    'country': 'India',
    'city': 'Delhi',
    'address': {
        'street': 'A 380, J J Colony, Shakarpur',
        'state': 'Delhi',
        'phone_no': '01127193524',
        'Zip code': '110092',
    }
}

print("Length of the dictionary: {}".format(len(student)))
print("\nDatatype of skills key: {}".format(
    type(student['skills'])))

student['skills'].append('ReactJs')
student['skills'].append('NodeJs')
print("\nSkills: {}".format(student['skills']))
print("\nValues of the dictionary:\n{}".format(list(student.values())))
print("\nDictionary items:\n{}".format(student.items()))
