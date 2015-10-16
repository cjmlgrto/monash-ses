# Unit CLASS
# - An object that represents every unique unit

# Class Dependencies: 
# - n/a

# Attributes: 
# - code, the unique unit code (e.g. "FIT1010") 
# - title, the name of a unit (e.g. "Introduction to Software Engineering")
# - description, the description of a unit
# - sequencesOffered, which semester and location it is offered in (e.g. "S2 CLAYTON")
# - yearOffered, which year it is offered in (e.g. "2015")
# - courseList, a list of included courses in a unit
# - studentList, a list of included students in a unit

class Unit:
    
    def __init__(self):
        self.code = ''
        self.title = ''
        self.description = ''
        self.sequencesOffered = []
        self.yearOffered = ''
        self.courseList = []
        self.studentList = []

    # GET ATTRIBUTES
        
    def getCode(self):
        return self.code
        
    def getTitle(self):
        return self.title
        
    def getDescription(self):
        return self.description
        
    def getSequencesOffered(self):
        return self.sequencesOffered
        
    def getYearOffered(self):
        return self.yearOffered
        
    def getCourseList(self):
        return self.courseList

    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        self.code = newCode
        
    def setTitle(self,newTitle):
        self.title = newTitle
        
    def setDescription(self,newDescription):
        self.description = newDescription
        
    def setSequencesOffered(self,newSequencesOffered):
        self.sequencesOffered.append(newSequencesOffered)
        
    def setYearOffered(self,newYearOffered):
        self.yearOffered = newYearOffered
        
    def setCourseList(self,newCourseList):
        self.courseList.append(newCourseList)
		
	# CLASS-SPECIFIC METHODS

    def displayDetails(self):
        return 'Unit Code: ' + self.code + ', Title: ' + self.title

    def addStudent(self,ID):
        self.studentList.append(ID)
