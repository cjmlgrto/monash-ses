__author__ = 'Josh'

from Course import Course
from Student import Student
from Unit import Unit
from University import University

'''CARLOS, use this file to run tests :) '''

testCourse = Course()
testStudent = Student()
testUnit = Unit()

def testOfStudentDisplayDetails():
    testStudent.setName('Joshua', 'Nelsson-Smith')
    testStudent.setStudID('25954113')
    print(testStudent.getName())
    print(testStudent.displayDetails())
    del testStudent

def