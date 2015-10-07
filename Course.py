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
        # todo: validation for type, maybe let the user select from a list
        self.type = newType
        
    def setName(self,newName):
        self.name = newName
        
    def unitList(self,newUnitList):
        self.unitList.append(newUnitList)
        
    