from student import Student
from course import Course
from teacher import Teacher
from SIS import SIS

def main():
    # Instantiate objects
    student1 = Student(Student_id=1, First_Name="John", Last_Name="Doe")
    course1 = Course(Course_ID=101, Course_Name="Mathematics")
    teacher1 = Teacher(Teacher_ID=1, First_Name="Jane", Last_Name="Smith")

    sis = SIS()

    try:
        # Add enrollment
        sis.AddEnrollment(student1, course1, enrollmentDate="2024-03-26")
        # Assign course to teacher
        sis.AssignCourseToTeacher(course1, teacher1)
        # Add payment
        sis.AddPayment(student1, amount=100, paymentDate="2024-03-26")

        # Get enrollments for a student
        sis.GetEnrollmentsForStudent(student1)
        # Get courses for a teacher
        sis.GetCoursesForTeacher(teacher1)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
