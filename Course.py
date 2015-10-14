class Course:
    
    def __init__(self):
        self.code = ''
        self.type = ''
        self.name = ''
        self.unitList = []
        
    # GET ATTRIBUTES
    
    def getCode(self):
        return self.code
        
    def getType(self):
        return self.type
        
    def getName(self):
        return self.name
        
    def getUnitList(self):
        return self.unitList
        
    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        self.code = newCode
        
    def setType(self,newType):
        self.type = newType
        
    def setName(self,newName):
        self.name = newName
        
    def AddToUnitList(self,newUnitList):
        self.unitList.append(newUnitList)

    def displayDetails(self):
        return 'Course Code: ' + self.code + ', Course Title: ' + self.name