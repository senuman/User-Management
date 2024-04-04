class Employee():
    def _init_(self, name, email, employee_id, department):
        super()._init_(name, email)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print("Type: Employee")