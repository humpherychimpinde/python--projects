# Function to calculate grade
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Students names and marks
students = ["Alice", "Bob", "Charlie", "David", "Eve",]
marks = [95,82,67,74,89]

# Loop through students and print grades
for i in range(len(students)):
    grade = calculate_grade(marks[i])
    print(f"{students[i]}: {marks[i]} - Grade {grade}") 
