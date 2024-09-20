import sqlite3
import datetime  # Import for getting current date and time

from opencv_learn.OwnProject.CreateDatabase import conn


def insert_student(id, name, student_class):
  """Inserts a new student record into the Students table.

  Args:
      id: Student's ID (integer).
      name: Student's name (text).
      student_class: Student's class (text).
  """
  conn = sqlite3.connect("students.db")
  cursor = conn.cursor()

  # Insert student data
  cursor.execute("""
  INSERT INTO Students (id, name, class, attendance_count) VALUES (?, ?, ?, ?)
  """, (id, name, student_class, 0))  # Initial attendance count: 0

  conn.commit()
  conn.close()

def mark_attendance(student_id):
  """Marks a student present and updates the attendance record.

  Args:
      student_id: ID of the student (integer).
  """
  conn = sqlite3.connect("students.db")
  cursor = conn.cursor()

  # Get current date and time
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS

  # Insert attendance record with current date and time
  cursor.execute("""
  INSERT INTO Attendance (student_id, date, status) VALUES (?, ?, ?)
  """, (student_id, date_time, "present"))

  # Update attendance count for the student
  cursor.execute("""
  UPDATE Students SET attendance_count = attendance_count + 1
  WHERE id = ?
  """, (student_id,))

  conn.commit()
  conn.close()

# Example student data (replace with your actual data)
students = [
    (100, "100", "MCA"),
    (101, "prateek", "MCA"),
    (102, "jaydeep", "MCA"),
  (103,"bhagirath","MCA"),
]

# Populate Students table
for student in students:
  insert_student(*student)  # Use unpacking for efficient insertion

# Example attendance update (replace with ID from face recognition)
# mark_attendance(2)  # Assuming student ID 2 is Bob

conn.close()  # Optional, connection closed within functions already
