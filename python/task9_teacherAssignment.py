import pyodbc


def assign_teacher_to_course(conn, course_code, teacher_name, teacher_email, teacher_expertise):
    try:
        cursor = conn.cursor()

        # Retrieve the course record from the database based on the course code
        cursor.execute("SELECT * FROM courses WHERE Course_Code = ?", (course_code,))
        course_record = cursor.fetchone()

        if course_record:
            # Assign Sarah Smith as the instructor for the course
            cursor.execute(
                "UPDATE courses SET Instructor_Name = ?, Instructor_Email = ?, Instructor_Expertise = ? WHERE Course_Code = ?",
                (teacher_name, teacher_email, teacher_expertise, course_code))
            print("Teacher assigned to the course successfully.")
            conn.commit()
        else:
            print("Course not found.")

    except pyodbc.Error as e:
        print(f"Error assigning teacher to course: {e}")
        conn.rollback()
    finally:
        cursor.close()


try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=server_name;DATABASE=SISDB; ')

    # Teacher's details
    teacher_name = 'Sarah Smith'
    teacher_email = 'sarah.smith@example.com'
    teacher_expertise = 'Computer Science'

    # Course to be assigned
    course_code = 'CS302'

    assign_teacher_to_course(conn, course_code, teacher_name, teacher_email, teacher_expertise)

except pyodbc.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()
