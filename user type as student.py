class Student: 
    'common base class for all students'
    count = 0
    
    def _init_(self, name, rollno):
         self.name = name
         self.rollno = rollno
         Student.count += 1
     
    def displayCount(self):
        print ("total no of Student %d" % Student.count)
    
    def showStudent(self):
        print ("Student name : ", self.name, ", rollno: ", self.rollno)