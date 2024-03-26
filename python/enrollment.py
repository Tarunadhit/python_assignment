class Enrollment:
    def __init__(self, enrollment_id=None, student=None, course=None, enrollment_date=None):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course
