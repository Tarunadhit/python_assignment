class Course:
    def __init__(self, course_id=None, course_name=None, course_code=None, instructor_name=None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.course_assigned = []
        self.enrolled_students = []
        self.enrollments = []

    def assign_teacher(self, teacher):
        if teacher not in self.course_assigned:
            self.course_assigned.append(teacher)
            print(f"{teacher.first_name} has been assigned to the course {self.course_name}")
        else:
            print(f"{teacher.first_name} has already been assigned to this course")

    def assign_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            self.enrollments.append((student.student_id, self.course_id))
            print(f"{student.first_name} has been enrolled in the course {self.course_name}")
        else:
            print(f"{student.first_name} is already enrolled in this course")

    def update_course_info(self, course_name, course_code, instructor_name):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name

    def display_course_info(self):
        print('-' * 50)
        print("Course Detail: ")
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Course Code:", self.course_code)
        print("Instructor Name:", self.instructor_name)

    def get_enrollments(self):
        print("Enrolled Students:")
        for student_id, course_id in self.enrollments:
            print(f"Student ID: {student_id} is enrolled in the course {self.course_code}")

    def get_teacher(self):
        print("Assigned Teacher(s):")
        for teacher in self.course_assigned:
            print(f"Teacher ID: {teacher.teacher_id}, Name: {teacher.first_name} {teacher.last_name}")
