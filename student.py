__author__ = 'Josh'


class Student:
    """ Class to represent every new instance of a unit, including every unit's attributes
        
        Dependencies - None
        
        Attributes:
            - studID, e.g. 26928523
            - unitArray, e.g. list of units in student
            - studFname, e.g. "Carlos"
            - studLname, e.g. "Melegrito"
            - degreeType, e.g. "Bachelor's"
            - residencyType, e.g. "International"
            - studyType, e.g. "Local"
            - courseCode, e.g. "CS678912987"
    
    """

    def __init__(self):
        """
        :purpose: initialises new student class
        :param (attribute): see attribute descriptions above
        :return: an initialised student
        """
        self.studID = ''
        self.unitArray = []
        self.studFname = ''
        self.studLname = ''
        self.degreeType = ''
        self.residencyType = ''
        self.studyType = ''
        self.courseCode = ''

    def getStudID(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.studID

    def setStudID(self, val):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.studID = val

    def getName(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.studFname + ' ' + self.studLname

    def setLName(self, lname):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.studLname = lname

    def setFName(self, fname):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.studFname = fname

    def getDegreeType(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.degreeType

    def setDegreeType(self, val):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.degreeType = val

    def getResidencyType(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.residencyType

    def setResidencyType(self, val):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.residencyType = val

    def getCourseCode(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.courseCode

    def setCourseCode(self, val):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.courseCode = val

    def getStudyType(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.studyType

    def setStudyType(self, val):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.studyType = val

    def displayDetails(self):
        """
        :purpose: returns all attributes
        :param (attribute): see attribute descriptions above
        :return: all attributes
        """
        string = 'Student ID: ' + str(self.getStudID()) + ', Name: ' + str(self.getName())
        return string

    def addUnit(self, unitCode):
        """
        :purpose: adds a new unit to the unitList attribute
        :param (attribute): see attribute descriptions above
        :return: adds a new unit to the unitList attribute
        """
        self.unitArray.append(unitCode)
