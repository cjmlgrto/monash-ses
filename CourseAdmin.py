__author__ = 'Josh'

from University import University
from Course import Course
from Unit import Unit
from Student import Student

class CourseAdmin:

    def __init__(self):
        pass

    def createStudent(self, studID, uniObject):

        studObject = Student()
        studObject.setStudID(str(studID))

        studLName = input("Please enter the student last name: ")
        studObject.setLName(studLName)

        studFName = input("Please enter the student first name: ")
        studObject.setFName(studFName)

        degreeType = input("Please enter the student's degree type (U for undergraduate or P for postgraduate): ")
        studObject.setDegreeType(degreeType)

        residencyType = input("Please enter the student's residency type (I for International, or D for Domestic):  ")
        studObject.setResidencyType(residencyType)

        studyType = input("Please enter the student's study type (F for full time, P for part time): ")
        studObject.setStudyType(studyType)

        print("\nSUCCESS: STUDENT RECORD CREATED\n")
        print(studObject.displayDetails())

        uniObject.addStudent(studObject)

    def createUnit(self, uniObject):

        unitObject = Unit()
        unitCode = input("Please enter Unit Code: ")
        unitObject.setCode(unitCode)

        unitTitle = input("Please enter Unit Title: ")
        unitObject.setTitle(unitTitle)

        print("\nSUCCESS: UNIT RECORD CREATED")
        print(unitObject.displayDetails())

        uniObject.addUnit(unitObject)

    def createCourse(self, uniObject):
        courseObject = Course()
        courseCode = input("Please enter Course Code: ")
        courseObject.setCode(courseCode)

        courseName = input("Please enter Course Name: ")
        courseObject.setName(courseName)

        print("\nSUCCESS: COURSE RECORD CREATED")
        print(courseObject.displayDetails())

        uniObject.addCourse(courseObject)





