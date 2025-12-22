  
import sqlite3

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll INTEGER,
    course TEXT
)
""")
conn.commit()

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    course = input("Enter Course: ")

    cursor.execute("INSERT INTO students (name, roll, course) VALUES (?, ?, ?)",
                   (name, roll, course))
    conn.commit()
    print(" Student Added Successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nID | Name | Roll | Course")
    print("-" * 30)
    for row in rows:
        print(row)

def update_student():
    sid = input("Enter Student ID to Update: ")
    name = input("Enter New Name: ")
    course = input("Enter New Course: ")

    cursor.execute("UPDATE students SET name=?, course=? WHERE id=?",
                   (name, course, sid))
    conn.commit()
    print(" Student Updated Successfully")

def delete_student():
    sid = input("Enter Student ID to Delete: ")
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    print(" Student Deleted")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank You ")
        break
    else:
        print(" Invalid Choice")
