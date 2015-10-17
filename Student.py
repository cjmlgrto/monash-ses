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
        self.fName = ''
        self.lName = ''
        self.degreeType = ''
        self.residencyType = ''
        self.studyType = ''
        self.course = ''
        self.units = []
        self.campus = ''
        
    # GET ATTRIBUTES
    
    def getID(self):
        return self.ID
        
    def getName(self):
        return self.fName + ' ' + self.lName
    
    def getDegreeType(self):
        return self.degreeType
		
    def getResidencyType(self):
        return self.residencyType
		
    def getCourse(self):
        return self.course
		
    def getStudyType(self):
        return self.studyType
		
    def displayDetails(self):
        print(self.ID + " - " + self.fName + " " + self.lName)

    def getCampus(self):
        return self.campus
    
    # SET ATTRIBUTES

    def setID(self, newID):
        self.ID = newID

    def setLName(self, newLName):
        self.lName = newLName

    def setFName(self, newFName):
        self.fName = newFName

    def setDegreeType(self, newDegreeType):
        self.degreeType = newDegreeType

    def setResidencyType(self, newResidencyType):
        self.residencyType = newResidencyType

    def setCourse(self, newCourse):
        self.course = newCourse

    def setStudyType(self, newStudyType):
        self.studyType = newStudyType

    def addUnit(self, unitCode):
        self.units.append(unitCode)

    def setCampus(self, campus):
        self.campus = campus
    
