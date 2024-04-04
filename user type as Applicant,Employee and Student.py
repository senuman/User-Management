class Person:
    def _init_(self, name, email):
        self.email = email
        self.name = name
     
    def display_details(self):
        pass  

class Student(Person):
    def __init__(self, name, email, student_id):
        super()._init_(name, email)
        self.student_id = student_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print("Type: Student")

class Employee(Person):
    def __init__(self, name, email, employee_id, department):
        super()._init_(name, email)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print("Type: Employee")
class Applicant(Person):
    def __init__(self, name, email, application_id):
        super()._init_(name, email)
        self.application_id = application_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Application ID: {self.application_id}")
        print(f"Email: {self.email}")
        print("Type: Applicant")

# Creating User Instances
student = Student(name="Tayyaba Amin", email="tayyaba071@gmail.com", student_id="F056")
employee = Employee(name="Arooj Fatima", email="arooj123@gmail.com", employee_id="A254", department="SE")
applicant = Applicant(name="Minahil", email="minahil101@gmail.com", application_id="M002")

# Displaying User Information
student.display_details()
print("\n")
employee.display_details()
print("\n")
applicant.display_details()
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
