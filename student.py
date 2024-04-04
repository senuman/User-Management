class Student():
    def _init_(self, name, email, student_id):
        super()._init_(name, email)
        self.student_id = student_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print("Type: Student")

