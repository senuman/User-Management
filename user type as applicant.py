class Applicant: 
    emptotal = 0
    
    def __init__(self, name, email,application_id):
         self.name = name
         self.email = email
         self.application_id = application_id
         Applicant.emptotal += 1
     
    def displayCount(self):
         print ("total no of Applicant %d" % Applicant.emptotal)
    
    def showApplicant(self):
         print ("Applicant name : ", self.name, ", salary: ", self.salary ,"application_id : ",self.application_id)

