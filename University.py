__author__ = 'Josh'

class University:

    def __init__(self):
        self.title = ''
        self.studentList = []
        self.unitList = []
        self.courseList = []

    def getTitle(self):
        return self.title

    def setTitle(self, val):
        self.title = val

    def displayStudents(self):
        print("Number of students in" + str(self.title) + "is " + str(len(self.studentList)))
        for student in self.studentList:
            student.displayDetails()

    def displayUnits(self):
        pass

    def displayCourses(self):
        pass
