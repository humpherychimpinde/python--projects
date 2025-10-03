# File to store student records
FILENAME = "records.txt"

# Function to add a student
def add_student(name,age,major):
    with open(FILENAME, "a") as file:
        file.write(f"{name},{age},{major}\n")
    print(f"Student{name} added successfully!")

# Function to view all students
def view_students():
    try:
       with open(FILENAME, "r") as file:
           students = file.readlines()
           if not students:
               print("No student Records found.")
               return
           print("\n=== Student Records ===")
           for line in students:
               name, age, major = line.strip().split(",")
               print(f"Name: {name}, Age: {age}, Major: {major}")            
    except FileNotFoundError:
        print("No records file found. Please add students first.")



# Add at least 5 students (will only add once,comment out after first run)
add_student("Alice", 20, "Computer Science")
add_student("Chipo", 21, "Mechanical Engineering")
add_student("David", 22, "Information Technology")
add_student("Bob", 21, "Teaching")
add_student("Bright", 25, "Electrical Engineering")


# view all students
view_students()
