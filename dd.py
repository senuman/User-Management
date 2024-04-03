class person:
    def __init__(self, name, CNIC, father_name, roll_number):
        self.name = name
        self.CNIC = CNIC
        self.father_name = father_name
        self.roll_number = roll_number

user = person("hamza", "31102", "kashif", "2051")

print(user.name, user.CNIC)