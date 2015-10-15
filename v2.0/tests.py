__author__ = 'Josh'

from Course import Course
from Student import Student
from Unit import Unit
from University import University

'''CARLOS, use this file to run tests :) '''


def testOfStudentDisplayDetails():

    testStudent = Student()
    testStudent.setName('Joshua', 'Nelsson-Smith')
    testStudent.setStudID('25954113')
    print(testStudent.displayDetails())
    del testStudent

def testOfUnitDisplayDetails():

    testUnit = Unit()
    testUnit.setCode('FIT1010')
    testUnit.setTitle('Introduction to Software Engineering')
    print(testUnit.displayDetails())
    del testUnit

def testOfCourseDisplayDetails():

    testCourse = Course()
    testCourse.setCode('2770')
    testCourse.setName('Bachelor of Software Engineering')
    print(testCourse.displayDetails())
    del testCourse

#testOfStudentDisplayDetails()
#testOfUnitDisplayDetails()
#testOfCourseDisplayDetails()

def testOfDictionaries():
    uni = University('Monash')
    stud = Student()
    stud.studID = '100'
    uni.addStudent(stud)
    print(uni.studentList)
    studtest = uni.studentList['100']
    print(studtest)

testOfDictionaries()