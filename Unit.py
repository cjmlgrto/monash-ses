class Unit:
    
    def __init__(self):
        self.code = ''
        self.title = ''
        self.description = ''
        self.sequencesOffered = []
        self.yearOffered = ''
        self.courseList = []
        self.prereqList = []
        self.coreqList = []
        self.prohibList = []
        
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
        
    def getPrereqList(self):
        return self.prereqList
        
    def getCoreqList(self):
        return self.coreqList
        
    def getProhibList(self):
        return self.prohibList
        
    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        self.code = newUnitCode
        
    def setTitle(self,newTitle):
        self.title = newUnitTitle
        
    def setDescription(self,newDescription):
        self.description = newUnitDescription
        
    def setSequencesOffered(self,newSequencesOffered):
        self.sequencesOffered.append(newSequencesOffered)
        
    def setYearOffered(self,newYearOffered):
        self.yearOffered = newYearOffered
        
    def setCourseList(self,newCourseList):
        self.courseList.append(newCourseList)
        
    def setPrereqList(self,newPrereqList):
        self.prereqList.append(newPrereqList)
        
    def setCoreqList(self,newCoreqList):
        self.coreqList.append(newCoreqList)
        
    def setProhibList(self,newProhibList):
        self.prohibList.append(newProhibList)
