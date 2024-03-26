import pyodbc


class SISDatabase:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = pyodbc.connect(connection_string)
        self.cursor = self.connection.cursor()

    def initialize_database(self):
        # Implement SQL scripts or code-first migration to create tables
        # Execute necessary SQL commands to create tables
        try:
            # Example SQL script to create Students table
            self.cursor.execute('''
                CREATE TABLE Students (
                    Student_ID INT PRIMARY KEY,
                    First_Name NVARCHAR(50),
                    Last_Name NVARCHAR(50),
                    DOB DATE,
                    Email NVARCHAR(100),
                    Phone_NO NVARCHAR(20)
                )
            ''')
            self.connection.commit()
        except Exception as e:
            print("Error initializing database:", e)

    def retrieve_students(self):
        # Implement method to retrieve student data from the database
        try:
            self.cursor.execute("SELECT * FROM Students")
            students = self.cursor.fetchall()
            return students
        except Exception as e:
            print("Error retrieving students:", e)

    def retrieve_courses(self):
        # Implement method to retrieve course data from the database
        try:
            self.cursor.execute("SELECT * FROM Courses")
            courses = self.cursor.fetchall()
            return courses
        except Exception as e:
            print("Error retrieving courses:", e)

    def insert_student(self, student_data):
        # Implement method to insert new student data into the database
        try:
            self.cursor.execute('''
                INSERT INTO Students (Student_ID, First_Name, Last_Name, DOB, Email, Phone_NO)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', student_data)
            self.connection.commit()
            print("Student inserted successfully.")
        except Exception as e:
            print("Error inserting student:", e)

    # Implement similar methods for other operations (e.g., enrollments, payments)

    def execute_query(self, query):
        # Implement method to execute custom SQL queries using parameterized queries
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print("Error executing query:", e)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


# Example usage:
connection_string = "DRIVER={SQL Server};SERVER=DESKTOP-SRA8EHN;DATABASE=SISDB;UID=;PWD="
sis_db = SISDatabase(connection_string)
sis_db.initialize_database()

sis_db.close_connection()
