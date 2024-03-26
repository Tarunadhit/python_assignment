class Teacher:
    def __init__(self, teacher_id=None, first_name=None, last_name=None, email=None):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def display_teacher_info(self):
        print('-' * 50)
        print("Teacher Info:")
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def update_teacher_info(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def assign_to_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)
            print('-' * 50)
            print(f"Teacher {self.first_name} assigned to course {course.course_name}")
        else:
            print('-' * 50)
            print(f"Teacher {self.first_name} is already assigned to course {course.course_name}")

    def get_assigned_courses(self):
        print('-' * 50)
        print(f"Courses assigned to Teacher {self.first_name}:")
        for course in self.assigned_courses:
            print(f"{course.course_id}-{course.course_name}")
