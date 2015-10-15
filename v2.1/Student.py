# Student CLASS
# - An object that represents every unique student

# Class Dependencies: 
# - n/a

# Attributes: 
# - ID, the unique student id (e.g. "26928523")
# - units, a list of included units in a student 
# - fName, a student's first name (e.g. "Carlos")
# - lName, a student's surname (e.g. "Melegrito")
# - degreeType, undergraduate/postgraduate
# - residencyType, local/international
# - studyType, full-time/part-time
# - courseCode, the code of a course that every unique student is enrolled in (e.g. "S3001")


class Student:

    def __init__(self):
        self.ID = ''
        self.units = []
        self.fName = ''
        self.lName = ''
        self.degreeType = ''
        self.residencyType = ''
        self.studyType = ''
        self.courseCode = ''
        
    # GET ATTRIBUTES
    
    def getID(self):
        return self.ID
        
    def getName(self):
        return self.fName + ' ' + self.lName
    
    def getDegreeType(self):
        return self.degreeType
		
    def getResidencyType(self):
        return self.resIDencyType
		
    def getCourseCode(self):
        return self.courseCode
		
    def getStudyType(self):
        return self.studyType
    
    # SET ATTRIBUTES

    def setID(self, newID):
        self.ID = newID

    def setLName(self, newLName):
        self.lName = newlName

    def setFName(self, newFName):
        self.fName = newfName

    def setDegreeType(self, newDegreeType):
        self.degreeType = newDegreeType

    def setResidencyType(self, newResidencyType):
        self.resIDencyType = newResidencyType

    def setCourseCode(self, newCourseCode):
        self.courseCode = newCourseCode

    def setStudyType(self, newStudyType):
        self.studyType = newStudyType
		
	# CLASS-SPECIFIC METHODS

    def displayDetails(self):
        string = 'Student ID: ' + str(self.getID()) + ', Name: ' + str(self.getName())
        return string

    def addUnit(self, unitCode):
        self.units.append(unitCode)
