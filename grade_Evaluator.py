# Ask for student details 
name = input("Enter student name: ")
score = int(input("Enter score (0-100):"))

# Determine grade 
if score >= 90 and score <= 100:
      grade = "A"
elif score >= 80 and score <= 89:
      grade = "B"
elif score >= 70 and score <=79:
      grade = "C"
elif score >= 60 and score <=69:
      grade = "D"
elif score >= 0 and score < 60:
      grade = "F"
else:
      grade ="Invalid score"

# Print result
print("\n--- Result ---")
print(f"Student: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")


