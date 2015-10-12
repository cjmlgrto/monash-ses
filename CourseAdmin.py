__author__ = 'Josh'

from University import University
from Course import Course
from Unit import Unit
from Student import Student


def createStudent(studID):

    studObject = str(studID)
    studObject = Student()
    studObject.setStudID(str(studID))

    studLName = input("Please enter the student last name")
    studObject.setLname(studLName)

    studFName = input("Please enter the student first name")
    studObject.setFName(studFName)

    degreeType = input("Please enter the student's degree type (U for undergraduate or P for postgraduate)")
    studObject.setDegreeType(degreeType)

    residencyType = input("Please enter the student's residency type (I for International, or D for Domestic ")
    studObject.setResidencyType(residencyType)

    studyType = input("Please enter the student's study type (F for full time, P for part time")
    studObject.setStudyType(studyType)


def createUnit(self):
        pass

def createCourse(self):
        pass

def enrollStudent(self):
        pass

