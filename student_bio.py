# Store 5 students in a list (names, ages and majors)
students = [ {"name": "Chipo", "age": 21, "major": "Computer science"}, {"name": "Bob", "age": 23, "major": "Mechanical Engineering"}, {"name": "Alice", "age": 22, "major": "Business Admistrator"}, {"name": "Frank", "age": 25, "major": "Teaching"}, {"name": "Bright", "age": 24, "major": "Electrician"} ]

# Print all student bios neatly
print("=== Student Bios ===\n")
for student in students:
    print(f"Student Name:{student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}\n")
