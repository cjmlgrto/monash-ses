# University CLASS
# - A database of students, units and courses

# Class Dependencies: 
# - Course, (Course.py)
# - Unit, (Unit.py)
# - Student, (Student.py)

# Attributes: 
# - students, a dictionary/list of students in a University object
# - units, a dictionary/list of units in a University object
# - courses, a dictionary/list of courses in a University object
# - title, the unique title of a University object (e.g. "Monash")
# - baseID, an integer representing the very first student ID to be generated from for each new student (increments by 1 per new student created)

from Course import Course
from Unit import Unit
from Student import Student


class University:
	
	def __init__(self,title):
		self.students = {}
		self.units = {}
		self.courses = {}
		self.title = title
		self.baseID = 10000000
		
	# GET ATTRIBUTES
	
	def getTitle(self):
		return self.title
		
	def displayStudents(self):
		print("\n" +
		str(self.title) + " has " + str(len(self.students)) + " students."
		)
		for ID, student in self.students.items():
			print(student.displayDetails())	
		
	def displayUnits(self):
		print("\n" +
		str(self.title) + " has " + str(len(self.units)) + " units."
		)
		for code, unit in self.units.items():
			print(student.displayDetails())
			
	def displayCourses(self):
		print("\n" +
		str(self.title) + " has " + str(len(self.courses)) + " courses."
		)
		for code, course in self.courses.items():
			print(course.displayDetails())
		
	# SET ATTRIBUTES
	
	def setTitle(self,newTitle):
		self.title = newTitle
		
	def addStudent(self,studentObject):
		if isinstance(studentObject, Student):
			self.students[studentObject.getID()] = studentObject
		else:
			print("\n" +
			"ERROR: " + studentObject + "is not a Student Object"
			)
			
	def addUnit(self,unitObject):
		if isinstance(unitObject, Unit):
			self.units[unitObject.getCode()] = unitObject
		else:
			print("\n" +
			"ERROR: " + unitObject + "is not a Unit Object"
			)
			
	def addCourse(self,courseObject):
		if isinstance(courseObject, Unit):
			self.units[courseObject.getCode()] = courseObject
		else:
			print("\n" +
			"ERROR: " + courseObject + "is not a Course Object"
			)
			
		
	# CHECKING ATTRIBUTE/OBJECT EXISTENCE
	
	def studentExists(self,ID):
		if ID in self.students:
			return True
		else:
			return False
			
	def unitExists(self,code):
		if code in self.units:
			return True
		else:
			return False
			
	def courseExists(self,code):
		if code in self.courses:
			return True
		else:
			return False
	