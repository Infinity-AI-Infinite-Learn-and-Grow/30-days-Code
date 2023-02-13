student={

    "first-name":"Yash",

    "Last-name":"Parmar",

    "gender":'M',

    "age":19,

    "marital_status":"Not Married",

    "skills":["Coding","Gaming","C++"],

    "Country":"India",

    "City":"Bhavnagar",

    "Address":"Ghogha Circle"

}

print(len(student))

print(student.get("skills"))

print(type(student.get("skills")))

print(student)

print("values as list")

for val in student.values():

        print(val)

print("Get the values as a list of tuple")

for key,value in student.items():

    print(key,"=>",value)
