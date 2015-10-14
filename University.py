from Student import Student
from Unit import Unit
from Course import Course

class University:

    def __init__(self, title):
        self.studentList = {}
        self.unitList = {}
        self.courseList = {}
        self.title = title

    def getTitle(self):
        return self.title

    def setTitle(self, val):
        self.title = val

    def displayStudents(self):
        print("\nNumber of students in " + str(self.title) + " is " + str(len(self.studentList)))
        for studID, student in self.studentList.items():
            print(student.displayDetails())

    def displayUnits(self):
        print("\nNumber of Units in " + str(self.title) + " is " + str(len(self.unitList)))
        for unitCode, unit in self.unitList.items():
            print(unit.displayDetails())

    def displayCourses(self):
        print("\nNumber of Courses in " + str(self.title) + " is " + str(len(self.courseList)))
        for courseCode, course in self.courseList.items():
            print(course.displayDetails())

    def addStudent(self, studentObject):
        if isinstance(studentObject, Student):
            self.studentList[studentObject.getStudID()] = studentObject
        else:
            print("ERROR: " + studentObject + " is not a Student Object")

    def addUnit(self, unitObject):
        if isinstance(unitObject, Unit):
            self.unitList[unitObject.getCode()] = unitObject
        else:
            print("ERROR: " + unitObject + " is not a Unit Object")

    def addCourse(self, courseObject):
        if isinstance(courseObject, Course):
            self.courseList[courseObject.getCode()] = courseObject
        else:
            print("ERROR: " + courseObject + " is not a Course Object")

    def courseExists(self, courseCode):
        if courseCode in self.courseList:
            return True
        else:
            return False

    def unitExists(self, unitCode):
        if unitCode in self.unitList:
            return True
        else:
            return False

    def studentExists(self, studentID):
        if studentID in self.studentList:
            return True
        else:
            return False
