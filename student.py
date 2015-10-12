__author__ = 'Josh'


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

    def getStudID(self):
        return self.studID

    def setStudID(self, val):
        self.studID = val

    def getName(self):
        return self.studFname + ' ' + self.studLname

    def setLName(self, lname):
        self.studLname = lname

    def setFName(self, fname):
        self.studFname = fname

    def getDegreeType(self):
        return self.degreeType

    def setDegreeType(self, val):
        self.degreeType = val

    def getResidencyType(self):
        return self.residencyType

    def setResidencyType(self, val):
        self.residencyType = val

    def getCourseCode(self):
        return self.courseCode

    def setCourseCode(self, val):
        self.courseCode = val

    def getStudyType(self):
        return self.studyType

    def setStudyType(self, val):
        self.studyType = val

    def displayDetails(self):
       string = 'Student ID: ' + str(self.getStudID()) + ', Name: ' + str(self.getName())
       return string

