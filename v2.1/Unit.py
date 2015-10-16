# Unit CLASS
# - An object that represents every unique unit

# Class Dependencies: 
# - n/a

# Attributes: 
# - code, the unique unit code (e.g. "FIT1010") 
# - title, the name of a unit (e.g. "Introduction to Software Engineering")
# - courses, a list of included courses in a unit
# - students, a list of included students in a unit

class Unit:
    
    def __init__(self):
        self.code = ''
        self.title = ''
        self.courses = []
        self.students = []

    # GET ATTRIBUTES
        
    def getCode(self):
        return self.code
        
    def getTitle(self):
        return self.title
        
    def getSequencesOffered(self):
        return self.sequencesOffered
        
    def getYearOffered(self):
        return self.yearOffered
		
    def displayDetails(self):
        print(self.code + " - " + self.title)

    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        self.code = newCode
        
    def setTitle(self,newTitle):
        self.title = newTitle
        
    def addCourse(self,newCode):
        self.courses.append(newCode)
		
    def addStudent(self,ID):
        self.students.append(ID)
