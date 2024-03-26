from enrollment import Enrollment
from payment import Payment


class Student:
    def __init__(self, student_id=None, first_name=None, last_name=None, dob=None, email=None, phone_no=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_no = phone_no
        self.enrolled_courses = []
        self.payment_made = []

    def enroll_in_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"Student {self.student_id} enrolled in course {course.course_id}")
        else:
            print(f"Student {self.student_id} is already enrolled in course {course.course_id}")

    def update_student_info(self, first_name, last_name, dob, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_no = phone_no

    def make_payment(self, payment):
        self.payment_made.append(payment)
        print(f"Payment of {payment.amount} made by {self.first_name} on {payment.payment_date}")

    def display_student_info(self):
        print('-' * 50)
        print("Students Detail: ")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_no}")

    def get_enrolled_courses(self):
        print('-' * 50)
        print(f"Enrolled Courses for {self.student_id}:")
        for course in self.enrolled_courses:
            print(f"{course.course_id}-{course.course_name}")

    def get_payment_history(self):
        print(f"Payment History for {self.student_id}: ")
        for payment in self.payment_made:
            print(f"Payment Amount: {payment.amount}, Date: {payment.payment_date}")
