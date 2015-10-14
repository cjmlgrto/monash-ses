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

    def displayDetails(self):
        return 'Unit Code: ' + self.code + ', Title: ' + self.title

    def addStudent(self, studID):
        self.studentList.append(studID)
