def get_student_name():
    """Prompt for student name and reject empty input."""
    while True:
        name = input("Enter student name: ").strip()
        if name: 
            return name 
        else: 
            print("Name cannot be empty. Please try again.")


def get_student_age():
    """Prompt for student age and only accept postive integers."""
    while True:
        age_input = input("Enter student age: ")
        try:                           
            age = int(age_input)
            if age > 0:
                return age 
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    students = []
    print("=== Student Input Validator ===") 
    for i in range(3):
        print(f"\nStudent {i + 1}:")
        name = get_student_name()
        age = get_student_age()
        students.append({"name": name, "age": age})
    print("\n Student Records: ")
    print("_" * 30)
    for s in students: 
        print(f"Name: {s['name']}, Age: {s['age']}")
    print("_" * 30)


if __name__ == "__name__":
    main()     
