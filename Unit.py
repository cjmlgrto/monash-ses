class Unit:
    """ Class to represent every new instance of a unit, including every unit's attributes
        
        Dependencies - None
        
        Attributes:
            - Code, e.g. FIT1010
            - Title, e.g. "Introduction to Software Engineering"
            - Description, e.g. "A unit about software engineering fundamentals"
            - Sequences Offered, i.e. what units are to be taken with this
            - Year Offered, e.g. "2015"
            - Student List, i.e. list of students in the unit
    
    """
    
    def __init__(self):
        """
        :purpose: initialises new units classes
        :param (attribute): see attribute descriptions above
        :return: an initialised unit
        """
        self.code = ''
        self.title = ''
        self.description = ''
        self.sequencesOffered = []
        self.yearOffered = ''
        self.courseList = []
        self.studentList = []

    # GET ATTRIBUTES
        
    def getCode(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.code
        
    def getTitle(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.title
        
    def getDescription(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.description
        
    def getSequencesOffered(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.sequencesOffered
        
    def getYearOffered(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.yearOffered
        
    def getCourseList(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.courseList

    # SET ATTRIBUTES
    
    def setCode(self,newCode):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.code = newCode
        
    def setTitle(self,newTitle):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.title = newTitle
        
    def setDescription(self,newDescription):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.description = newDescription
        
    def setSequencesOffered(self,newSequencesOffered):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.sequencesOffered.append(newSequencesOffered)
        
    def setYearOffered(self,newYearOffered):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.yearOffered = newYearOffered
        
    def setCourseList(self,newCourseList):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.courseList.append(newCourseList)

    def displayDetails(self):
        """
        :purpose: returns all attributes
        :param (attribute): see attribute descriptions above
        :return: all attributes
        """
        return 'Unit Code: ' + self.code + ', Title: ' + self.title

    def addStudent(self, studID):
        """
        :purpose: adds a new student to the studentList attribute
        :param (attribute): see attribute descriptions above
        :return: adds a new student to the studentList attribute
        """
        self.studentList.append(studID)
