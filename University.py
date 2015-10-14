__author__ = 'Josh'
from Student import Student
from Unit import Unit
from Course import Course

class University:
    """ Class to represent the University object, acts as a database for the student, unit and Course records.

        Dependencies - None

        Attributes - Title, the title you wish for the University

    """

    def __init__(self, title):
        """
        :purpose: Initialises university class
        :param title: the title of the university
        :return: an initialised university object
        """
        """
        :param title:
        :return:
        """
        self.studentList = {}
        self.unitList = {}
        self.courseList = {}
        self.title = title

    def getTitle(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        return self.title

    def setTitle(self, val):
        """
        :purpose: initialises a NEW attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        self.title = val

    def displayStudents(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        print("\nNumber of students in " + str(self.title) + " is " + str(len(self.studentList)))
        for studID, student in self.studentList.items():
            print(student.displayDetails())

    def displayUnits(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        print("\nNumber of Units in " + str(self.title) + " is " + str(len(self.unitList)))
        for unitCode, unit in self.unitList.items():
            print(unit.displayDetails())

    def displayCourses(self):
        """
        :purpose: returns attribute
        :param (attribute): see attribute descriptions above
        :return: adds the attribute to the class
        """
        print("\nNumber of Courses in " + str(self.title) + " is " + str(len(self.courseList)))
        for courseCode, course in self.courseList.items():
            print(course.displayDetails())

    def addStudent(self, studentObject):
        """
        :purpose: adds a new student to the studentList attribute
        :param (attribute): see attribute descriptions above
        :return: adds a new student to the studentList attribute
        """
        if isinstance(studentObject, Student):
            self.studentList[studentObject.getStudID()] = studentObject
        else:
            print("ERROR: " + studentObject + " is not a Student Object")

    def addUnit(self, unitObject):
        """
        :purpose: adds a new unit to the attribute
        :param (attribute): see attribute descriptions above
        :return: adds a new unit to the attribute
        """
        if isinstance(unitObject, Unit):
            self.unitList[unitObject.getCode()] = unitObject
        else:
            print("ERROR: " + unitObject + " is not a Unit Object")

    def addCourse(self, courseObject):
        """
        :purpose: adds a new course to the attribute
        :param (attribute): see attribute descriptions above
        :return: adds a new course to the attribute
        """
        if isinstance(courseObject, Course):
            self.courseList[courseObject.getCode()] = courseObject
        else:
            print("ERROR: " + courseObject + " is not a Course Object")

    def courseExists(self, courseCode):
        """
        :purpose: checks existence of a course
        :param (attribute): see attribute descriptions above
        :return: true, if it exists, false otherwise
        """
        if courseCode in self.courseList:
            return True
        else:
            return False

    def unitExists(self, unitCode):
        """
        :purpose: checks existence of a unit
        :param (attribute): see attribute descriptions above
        :return: true, if it exists, false otherwise
        """
        if unitCode in self.unitList:
            return True
        else:
            return False

    def studentExists(self, studentID):
        """
        :purpose: checks existence of a student
        :param (attribute): see attribute descriptions above
        :return: true, if it exists, false otherwise
        """
        if studentID in self.studentList:
            return True
        else:
            return False
