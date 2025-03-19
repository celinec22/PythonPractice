# Everything I Need to Know About Dictornarys (Key-Value Pairs)
# We can attribute something similar to HashMaps - or unordered_sets in C++

student = {"fname": "John", "age": 25, "courses": ["Math", "CompSci"]}

# Access Values through Key to get Value
print(student["fname"])

# Produces a KeyError
# print(student['phone'])

# Better Way to Access in the Case not found, no error is thrown
print(student.get("phone", "Not Found"))


# updating through assignment
student["fname"] = "Celine"

# creating new key value
student["lname"] = "Chahine"


# updating through update method (allows for reassignment of mutiple values)
# and also allows for the creation of new keys

student.update({"fname": "Jane", "phone": "313", "age": 33})


# delete from dictionary
del student["phone"]


# using pop method can help save the element before gettind rid of it

age = student.pop("age")

#
for key, value in student.items():
    print(key)
