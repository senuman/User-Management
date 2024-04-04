class Applicant():
    def __init__(self, name, email, application_id):
        super()._init_(name, email)
        self.application_id = application_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Application ID: {self.application_id}")
        print(f"Email: {self.email}")
        print("Type: Applicant")
        
print("try programiz.pro")