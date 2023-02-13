#Day8

student = {
  "first_name": "Kamri",
  "last_name": "Mcknight",
  "gender":"Female",
  "age":20,
  "marital_status":"single",
  "skills":["Nuerology"],
  "country":"USA",
  "city":"Texas",
  "Address":"4th street AD",  
}

#Length of dictionary
print("Lenght of dictionary : ",len(student))
print("\t")

#Value of skills and data type
print("Skills : ",student["skills"])
print("Data type of skills is : ",type(student["skills"]))
print("\t")

# Modify the skills values by adding one or two skills
student["skills"] += ["Chemistry", "Biology"]
print(student["skills"])
print("\t")

#dictionary values as a list
print("Student dictionary values : ", list(student.values()))
print("\t")

# dictionary to a list of tuples using the items() method
print("student dictionary as list of tuples : ",student.items())
print("\t")