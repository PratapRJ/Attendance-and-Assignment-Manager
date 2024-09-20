import sqlite3

conn = sqlite3.connect("students.db")  # Creates students.db if it doesn't exist
cursor = conn.cursor()

# Create the Students table with attendance count (default 0)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    attendance_count INTEGER
)
""")

# Modify the Attendance table to include date, status, and foreign key
cursor.execute("""
CREATE TABLE IF NOT EXISTS Attendance (
    student_id INTEGER,
    date TEXT,  -- Today's date and time will be inserted here
    FOREIGN KEY (student_id) REFERENCES Students(id)
)
""")

conn.commit()  # Save changes to the database
conn.close()  # Close the connection
