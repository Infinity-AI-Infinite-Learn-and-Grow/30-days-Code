"""Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary values as a list
Change the dictionary to a list of tuples using the items() method"""

dict={
  "first_name": "Shubham ",
  "last_name" : "bansal",
  "gender" : "male",
  "age":20,
  "marital status" :"Non-Married",
  "skills" :["java","python","C++","C"],
  "country" : "India",
  "city": "Delhi",
  "Address" : "pb,New delhi -1100000"
}

#length
print(len(dict))

#skill
print(dict["skills"])
#Type of values
print(type(dict["skills"]))

print(dict.items())


