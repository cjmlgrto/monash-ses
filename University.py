__author__ = 'Josh'
from Student import Student
from Unit import Unit
from Course import Course

class University:

    def __init__(self, title):
        self.title = title
        self.studentList = {}
        self.unitList = {}
        self.courseList = {}

    def getTitle(self):
        return self.title

    def setTitle(self, val):
        self.title = val

    def displayStudents(self):
        print("Number of students in " + str(self.title) + " is " + str(len(self.studentList)))
        for student in self.studentList:
            print(student.displayDetails())

    def displayUnits(self):
        print("Number of Units" + str(self.title) + "is " + str(len(self.unitList)))
        for unit in self.unitList:
            print(unit.displayDetails())


    def displayCourses(self):
        print("Number of Courses in" + str(self.title) + "is " + str(len(self.courseList)))
        for course in self.courseList:
            print(course.displayDetails())

    def addStudent(self, studentObject):
        if isinstance(studentObject, Student):
            self.studentList[studentObject.getStudID] = studentObject
        else:
            print("ERROR: " + studentObject + " is not a Student Object")

    def addUnit(self, unitObject):
        if isinstance(unitObject, Unit):
            self.unitList[unitObject.getCode] = unitObject
        else:
            print("ERROR: " + unitObject + " is not a Unit Object")

    def addCourse(self, courseObject):
        if isinstance(courseObject, Course):
            self.courseList[courseObject.getCode] = courseObject
        else:
            print("ERROR: " + courseObject + " is not a Course Object")
