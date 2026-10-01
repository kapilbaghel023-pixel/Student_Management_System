# Student_Management_System
Student Management System

A simple console-based Student Management System built with Python.
This project is designed to manage student admission details, additional information, result details, updating records, viewing records, and deleting student records using Python file handling.

---

📌 Project Overview

The Student Management System is a beginner-friendly Python project that demonstrates how Python can be used to build a basic real-world management application.

The project uses:

- Python Classes and Objects
- Methods
- Exception Handling
- File Handling
- Dictionaries
- Nested Dictionaries
- User Input
- String Manipulation
- Basic Calculations
- CRUD-like operations

Student records are stored in files using the student's roll number as the file name.

---

✨ Features

1. New Admission

Creates a new student record containing:

- Roll Number
- Student Name
- Class
- Previous Qualification
- Previous Institution
- Aadhaar Number
- Father's Name
- Mother's Name

The information is stored in a student-specific file.

2. Show Student Details

Allows the user to enter a student's roll number and view the stored details.

3. Add Extra Details

Additional information can be appended to an existing student's file.

4. Update Details

Allows the user to select a line and replace existing information with updated information.

5. Delete Student

Deletes the student's file using the student's roll number.

6. Add Result

Stores a basic report card containing:

- Subject names
- Subject marks
- Percentage

The percentage is calculated from three subjects.

7. Exit

Terminates the Student Management System.

---

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
File Handling| Store and manage student records
Dictionary| Organize student information
OOP| Structure the application using a class
Exception Handling| Handle input and file-related errors

---

🧠 Python Concepts Demonstrated

This project demonstrates several important Python concepts:

- "class"
- Objects
- Methods
- "try-except"
- "input()"
- String methods such as ".strip()" and ".lower()"
- Dictionaries
- Nested dictionaries
- "with open()"
- File modes: "r", "w", and "a"
- "read()"
- "readlines()"
- "write()"
- "writelines()"
- "os.remove()"
- Type conversion using "int()"
- Basic arithmetic operations
- "while" loop
- Conditional statements
- "return"
- Exception handling

---

📂 Project Structure

Student-Management-System/
│
├── student_management.py
└── README.md

«Student files are created automatically when a new admission is registered.»

Example:

Student-Management-System/
│
├── student_management.py
├── README.md
├── 101
├── 102
└── 103

Here, "101", "102", and "103" can represent student roll-number files.

---

▶️ How to Run

Step 1: Install Python

Make sure Python is installed on your system.

Check the Python version:

python --version

Step 2: Clone the Repository

git clone <your-repository-link>

Step 3: Open the Project Folder

cd Student-Management-System

Step 4: Run the Program

python student_management.py

The program will display the following menu:

--- Student Management System ---

1. New Admission
2. Show Details
3. Add Extra Detail
4. Update Detail
5. Delete Student
6. Add Result
7. Exit

Enter the corresponding option to perform an operation.

---

🔄 How the System Works

New Admission Flow

User
  ↓
Enter Student Details
  ↓
Create Student Dictionary
  ↓
Use Roll Number as File Name
  ↓
Store Data in File
  ↓
Student Record Created

Result Flow

Enter Roll Number
        ↓
Enter 3 Subjects
        ↓
Enter Marks
        ↓
Calculate Percentage
        ↓
Append Result to Student File

---

📊 Result Calculation

The project calculates the percentage using three subjects.

r = ((sub1 + sub2 + sub3) * 100) / 300

For example, if a student scores:

Subject 1 = 80
Subject 2 = 75
Subject 3 = 90

The total marks are calculated and converted into a percentage.

---

💾 Data Storage

The project currently uses Python file handling instead of a database.

Each student's roll number is used as the file name.

For example:

Roll Number: 101

creates a file similar to:

101

Student information is written into that file.

The project uses:

open(roll_no, "w")

for creating/writing records,

open(roll_no, "r")

for reading records,

and

open(roll_no, "a")

for adding additional information.

---

⚠️ Current Limitations

This project is intentionally built as a basic Python file-based management system.

Current limitations include:

- Data is stored in individual files rather than a database.
- The result system currently supports three subjects.
- Input validation is basic.
- Student records are stored as text representations of dictionaries.
- The update functionality works by modifying a selected line.
- There is no graphical user interface.
- There is no login or authentication system.

These limitations provide opportunities for future improvements.

---

🚀 Future Improvements

Possible future improvements include:

- Add database support using SQLite/MySQL
- Add proper student ID validation
- Add marks validation
- Add more subjects dynamically
- Add search functionality
- Add student attendance management
- Add GPA/CGPA calculation
- Add a graphical user interface using Tkinter
- Add proper structured data storage using JSON
- Improve input validation
- Add confirmation before deleting a student
- Improve the update system
- Generate printable student report cards

---

🎯 Learning Purpose

This project was created to practice Python programming concepts by applying them to a practical real-world problem.

It demonstrates how basic Python concepts can be combined to create a functional console-based application.

---

👨‍💻 Author

Kapil Baghel

Skills/Concepts Practiced

- Python
- Object-Oriented Programming
- File Handling
- Exception Handling
- Dictionaries
- Basic Data Management
- Console Application Development

---

📜 License

This project is created for learning and educational purposes.
