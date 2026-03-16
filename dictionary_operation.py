# Create and access dictionary elements
student = {
    "name": "Om",
    "age": 19,
    "course": "Computer Science"
}

print("Dictionary:", student)
print("Name:", student["name"])
print("Course:", student["course"])

# Update Dictionary
student["course"] = "Artificial Intelligence"
print("Updated Dictionary:", student)

# Removing Elements
student.pop("age")
print("Dictionary after removing element:", student)