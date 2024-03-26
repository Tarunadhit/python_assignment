import pyodbc


def generate_enrollment_report(course_name, conn):
    try:
        cursor = conn.cursor()
        # Retrieve enrollment records for the specified course
        cursor.execute("SELECT students.Student_ID, students.First_Name, students.Last_Name FROM enrollments "
                       "INNER JOIN students ON enrollments.student_id = students.Student_ID "
                       "INNER JOIN courses ON enrollments.course_id = courses.Course_ID "
                       "WHERE courses.Course_Name = ?", (course_name,))
        enrollment_records = cursor.fetchall()

        # Generate the enrollment report
        report = f"Enrollment Report for Course: {course_name}\n"
        report += "-------------------------------------------\n"
        report += "Student ID  |  First Name  |  Last Name\n"
        report += "-------------------------------------------\n"
        for record in enrollment_records:
            report += f"{record[0]} | {record[1]} | {record[2]}\n"

        # Display the report
        print(report)


    except Exception as e:
        print(f"Error generating enrollment report: {e}")


# Database connection parameters
server = 'localhost'
database = 'SISDB'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

# Construct the connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)

    # Generate the enrollment report for "Computer Science 101"
    generate_enrollment_report("Computer Science 101", conn)

except pyodbc.Error as e:
    print(f"Database error: {e}")

finally:
    # Close the database connection
    if conn:
        conn.close()
