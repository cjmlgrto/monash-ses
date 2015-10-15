class Student:

    def __init__(self):
        self.ID = ''
        self.units = []
        self.fName = ''
        self.lName = ''
        self.degreeType = ''
        self.resIDencyType = ''
        self.studyType = ''
        self.courseCode = ''
        
    # GET ATTRIBUTES
    
    def getID(self):
        return self.ID
        
    def getName(self):
        return self.fName + ' ' + self.lName
    
    def getDegreeType(self):
        return self.degreeType
		
    def getResIDencyType(self):
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

    def setResIDencyType(self, newResIDencyType):
        self.resIDencyType = newResIDencyType

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
