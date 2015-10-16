# Course CLASS
# - An object that represents every unique course

# Class Dependencies: 
# - n/a

# Attributes: 
# - code, the unique course code (e.g. "S3001") 
# - type, undergraduate/postgraduate
# - name, the name of a course (e.g. "Bachelor of Science Advanced (Honours)")
# - units, a list of included units in a course
# - students, a list of included students in a course


class Course:
    
    def __init__(self):
        self.code = ''
        self.type = ''
        self.name = ''
        self.units = []
		self.students = []
        
    # GET ATTRIBUTES
    
    def getCode(self):
        return self.code
        
    def getType(self):
        return self.type
        
    def getName(self):
        return self.name
        
    def getUnits(self):
        return self.units
		
	def displayDetails(self):
		print(self.code + " - " + self.name)
        
    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        self.code = newCode
        
    def setType(self,newType):
        self.type = newType
        
    def setName(self,newName):
        self.name = newName
		
    def addUnit(self, unitCode):
        self.units.append(unitCode)
		
    def addStudent(self,ID):
        self.students.append(ID)
		
   