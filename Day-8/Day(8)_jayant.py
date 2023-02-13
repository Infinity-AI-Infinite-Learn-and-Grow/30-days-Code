student={"First_name":"jayant","Last_name":"Agarwal","gender":"male","age":20,"martial status": "unmarried","skills":["android developer","python developer"],"country":"India","city":"bhubneshwar","address":"bhubneshwar"}
l=len(student)
print("length of dictionary is",l,"\n")

print(student["skills"],"\n")
print(type(student["skills"]),"\n")

student["skills"].append("web developer")
print(student["skills"],"\n")

print(student.values(),"\n")




item=student.items()
print(item)