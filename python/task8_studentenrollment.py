import pyodbc
from datetime import date


def add_student(conn, id, first_name, last_name, birth_date, email, phone):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (student_id, first_name, last_name, Date_of_birth, Gender, email, Phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)",
            id, first_name, last_name, birth_date, 'M', email, phone)  # Assuming 'M' for gender
        print("Data inserted successfully...")
        conn.commit()
    except pyodbc.Error as e:
        print(f"Error during student enrollment: {e}")
        conn.rollback()
    finally:
        cursor.close()


def enrol_student(conn, student_id, courses):
    try:
        cursor = conn.cursor()
        for course in courses:
            # Enroll the student in each specified course
            cursor.execute("INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
                           student_id, course, date.today())  # Assuming today's date for enrollment_date
        print(f"Student enrolled in courses successfully.")
        conn.commit()
    except pyodbc.Error as e:
        print(f"Error during course enrollment: {e}")
        conn.rollback()
    finally:
        cursor.close()


try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-SRA8EHN\SQLEXPRESS;DATABASE=SISDB;')
    id = 20
    first_name = 'John'
    last_name = 'Doe'
    birth_date = date(1995, 8, 15)
    email = 'john.doe@example.com'
    phone = '123-456-7890'
    add_student(conn, id, first_name, last_name, birth_date, email, phone)
    course_ids = [101, 112]  # Assuming course IDs are integers
    enrol_student(conn, id, course_ids)
except pyodbc.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()
