             #Dictionaries


students ={
    "name":"suve",
    "age":19,
    "grade":"+A"
}

# 1) Access the data
print(students)
print(students["name"])


# 2) adding and upadating 
students["name"] ="suvx"
students["address"] = "159 vannarapettai street, chennai"
print(students)

# 3)Delete or pop
del students["grade"]
students.pop("age")
print(students)


# 4) print in for loop order
student ={
    "name":"suve",
    "age":19,
    "grade":"+A"
}

for keyvalue in student.items():
    print(keyvalue)
