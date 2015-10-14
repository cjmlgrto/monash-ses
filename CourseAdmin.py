__author__ = 'Josh'

from University import University
from Course import Course
from Unit import Unit
from Student import Student

class CourseAdmin:

    def __init__(self):
        pass

    def createStudent(self, studID, uniObject):

        courseCode = input("Please enter the code for the Course the student is enrolled in: ")
        if uniObject.courseExists(courseCode):

            studObject = Student()
            studObject.setStudID(str(studID))

            studObject.setCourseCode(courseCode)

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

            return studID + 1

        else:
            print("ERROR: Course Code does not exist")
            return studID

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

    def enrollStudent(self, uniObject):
        studID = input("Please enter the student ID of the student you wish to enroll: ")
        if uniObject.studentExists(studID):
            unitCode = input("Please enter the unit code of the unit you wish to enroll in: ")
            if uniObject.unitExists(unitCode):
                unitObject = uniObject.unitList[unitCode]
                studentObject = uniObject.studentList[studID]
                unitObject.addStudent(studID)
                studentObject.addUnit(unitCode)
                uniObject.addUnit(unitObject)
                uniObject.addStudent(studentObject)

                print("SUCCESS: " + studentObject.getName() + " enrolled in " + unitObject.getCode())

            else:
                print("ERROR: Unit Code does not exist")
        else:
            print("ERROR: Student ID does not exist")





