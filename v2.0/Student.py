class Student:

    def __init__(self):
        self.studID = ''
        self.unitArray = []
        self.studFname = ''
        self.studLname = ''
        self.degreeType = ''
        self.residencyType = ''
        self.studyType = ''
        self.courseCode = ''
        
    # GET ATTRIBUTES
    
    def getStudID(self):
        return self.studID
        
    def getName(self):
        return self.studFname + ' ' + self.studLname
    
    def getDegreeType(self):
        return self.degreeType
		
    def getResidencyType(self):
        return self.residencyType
		
    def getCourseCode(self):
        return self.courseCode
		
    def getStudyType(self):
        return self.studyType
    
    # SET ATTRIBUTES

    def setStudID(self, val):
        self.studID = val

    def setLName(self, lname):
        self.studLname = lname

    def setFName(self, fname):
        self.studFname = fname

    def setDegreeType(self, val):
        self.degreeType = val

    def setResidencyType(self, val):
        self.residencyType = val

    def setCourseCode(self, val):
        self.courseCode = val

    def setStudyType(self, val):
        self.studyType = val

    def displayDetails(self):
        string = 'Student ID: ' + str(self.getStudID()) + ', Name: ' + str(self.getName())
        return string

    def addUnit(self, unitCode):
        self.unitArray.append(unitCode)
