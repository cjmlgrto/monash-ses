class Course:
    """ Class to represent every new instance of a unit, including every unit's attributes
        
        Dependencies - None
        
        Attributes:
            - Code, e.g. BSC0001
            - Name, e.g. "Bachelor of Science"
            - Type, e.g. "Diploma, or graduate degree, etc."
            - Unit list, i.e. list of units in the course
    
    """
    
    def __init__(self):
        """
        :purpose: initialises new units classes
        :param (attribute): see attribute descriptions above
        :return: an initialised course
        """
        self.code = ''
        self.type = ''
        self.name = ''
        self.unitList = []
        
    # GET ATTRIBUTES
    
    def getCode(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.code
        
    def getType(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.type
        
    def getName(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.name
        
    def getUnitList(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.unitList
        
    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.code = newCode
        
    def setType(self,newType):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        # todo: validation for type, maybe let the user select from a list
        self.type = newType
        
    def setName(self,newName):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.name = newName
        
    def AddToUnitList(self,newUnitList):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.unitList.append(newUnitList)

    def displayDetails(self):
        """
        :purpose: returns all attributes
        :param (attribute): see attribute descriptions above
        :return: all attributes
        """
        return 'Course Code: ' + self.code + ', Course Title: ' + self.name