class Employee: 
    'common base class for all employees'
    emptotal = 0
    
    def __init__(self, name, salary):
         self.name = name
         self.salary = salary
         Employee.emptotal += 1
     
    def displayCount(self):
         print ("total no of Employee %d" % Employee.emptotal)
    
    def showEmployee(self):
         print ("Employee name : ", self.name, ", salary: ", self.salary)

