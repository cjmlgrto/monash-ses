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
        return self.studFname + self.studLname

    def setName(self, fname, lname):
        self.studFname = fname
        self.studLname = lname

    def getDegreeType(self):
        return self.degreeType

    def setStudID(self, val):
        self.studID = val

    def getResidencyType(self):
        return self.residencyType

    def setStudID(self, val):
        self.studID = val

    def getCourseCode(self):
        return self.courseCode

    def setStudID(self, val):
        self.studID = val

    def getStudyType(self):
        return self.studyType

    def setStudID(self, val):
        self.studID = val

