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
            print(student.displayDetails())

    def displayUnits(self):
        print("Number of Units" + str(self.title) + "is " + str(len(self.unitList)))
        for unit in self.unitList:
            print(unit.displayDetails())


    def displayCourses(self):
        print("Number of Courses in" + str(self.title) + "is " + str(len(self.courseList)))
        for course in self.courseList:
            print(course.displayDetails())
