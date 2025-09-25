# Store student names and their marks
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [85,92,78,88,95]

# Function to assign grades
def assign_grade(score):              
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Print summary table
print("=== Student Marks Analyzer ===")  
for i in range(len(students)):
    grade = assign_grade(marks[i])
    print(f"{students[i]}: {marks[i]} - Grade {grade}")

# Calculate average
average = sum(marks) / len(marks)
print(f"\nAverage marks: {average:.if}")
