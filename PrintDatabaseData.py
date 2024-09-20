import sqlite3

conn = sqlite3.connect("students.db")  # Connect to the database
cursor = conn.cursor()

# Get table information
cursor.execute("PRAGMA table_info(Students)")  # Use PRAGMA for table info

# Print column names and data types
print("Students Table Info:")
print("---------------------")
for column in cursor.fetchall():
  print(f"Column Name: {column[1]} (Type: {column[2]})")

# Get all students
cursor.execute("SELECT * FROM Students")  # Select all columns from Students

# Print student data
print("Students:")
print("---------------------")
for student in cursor.fetchall():
  # Access student data by index
  id, name, student_class, attendance_count = student
  print(f"ID: {id}, Name: {name}, Class: {student_class}, Attendance Count: {attendance_count}")

# Get all students
cursor.execute("SELECT * FROM Attendance")  # Select all columns from Students

# Print student data
print("Attendance:")
print("---------------------")
for attendance in cursor.fetchall():
  # Access student data by index
  id, date= attendance
  print(f"ID: {id}, Date:{date}")

conn.close()  # Close the connection
