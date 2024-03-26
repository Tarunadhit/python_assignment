class Payment:
    def __init__(self, payment_id=None, student_id=None, amount=None, payment_date=None):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date

    def get_student_id(self):
        return self.student_id

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date