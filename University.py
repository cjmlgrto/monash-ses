__author__ = 'Josh'

class University:

    def __init__(self):
        self.title = ''
        self.studentList = []
        self.unitList = []
        self.courseList = []

    def displayStudents(self):
        print("Number of students in University is ")
        for student in self.studentList:
            student.displayDetails

    def displayUnits(self):
        pass

    def displayCourses(self):
        pass
