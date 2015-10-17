# CourseAdmin CLASS
# - All the functions required for the Student Enrolment System

# Class Dependencies: 
# - University, (University.py)
# - Course, (Course.py)
# - Unit, (Unit.py)
# - Student, (Student.py)
# - Validate, (Validate.py)

# Attributes: 
# - n/a


from University import University
from Course import Course
from Unit import Unit
from Student import Student
from Validate import Validate

validator = Validate()

class Enrolment:
	
	# UNIT METHODS
	
	# - Create Unit
	def createUnit(self,university):
		print("\n \n \n")
		print("CREATING A NEW UNIT:")
		newUnit = Unit()
		code = input("New unit code: ")
		code = validator.validateUnitCode(code)
		newUnit.setCode(code)
		title = input("New unit title: ")
		newUnit.setTitle(title)
		university.addUnit(newUnit)
		print("\nSUCCESS: UNIT RECORD CREATED: \n")
		newUnit.displayDetails()
		print("\n \n \n")
	
	# - Search Unit
	def searchUnit(self,university):
		print("\n \n \n")
		print("SEARCHING FOR A UNIT:")
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			unit = university.units[code]
			unit.displayDetails()
			print("Students enrolled in this unit:")
			for ID in unit.students:
				student = university.students[ID]
				print("\n" + student.fName + " " + student.lName + " (" + student.ID + ")")
		else:
			print("ERROR: Unit code does not exist")
		print("\n \n \n")
			
	# - Display All Units
	def displayAllUnits(self,university):
		print("\n \n \n")
		print("DISPLAYING ALL UNITS:")
		university.displayUnits()
		print("\n \n \n")
		
	# - Display Students in Unit
	def displayStudentsInUnit(self,university):
		print("\n \n \n")
		print("DISPLAYING STUDENTS IN A UNIT:")
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			unit = university.units[code]
			print(unit.title + " has " + len(unit.students) + " students:")
			for ID in unit.students:
				student = university.students[ID]
				print("\n" + student.fName + " " + student.lName + " (" + student.ID + ")")
		else:
			print("ERROR: Unit code does not exist")
		print("\n \n \n")
			
	# - Edit Unit Details
	def editUnitDetails(self,university):
		print("\n \n \n")
		print("EDITING UNIT DETAILS:")
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			university.units.pop(code, None)
			newUnit = Unit()
			code = input("New unit code: ")
			code = validator.validateUnitCode(code)
			newUnit.setCode(code)
			title = input("New unit title: ")
			newUnit.setTitle(title)
			university.addUnit(newUnit)
			print("\nSUCCESS: UNIT RECORD CREATED")
			newUnit.displayDetails()
		else:
			print("ERROR: Unit code does not exist")
		print("\n \n \n")
	
	# - Delete Unit
	def deleteUnit(self,university):
		print("\n \n \n")
		print("DELETING UNIT:")
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			unit = university.units[code]
			title = unit.title
			university.units.pop(code, None)
			print("\nSUCCESS: " + title + " has been deleted")
		else:
			print("ERROR: Unit code does not exist")
		print("\n \n \n")
	
	# STUDENT METHODS
	
	# - Create Student
	def createStudent(self,baseID,university):
		print("\n \n \n")
		print("ADDING A STUDENT TO UNIVERSITY:")
		courseCode = input("Enter a Course code: ")
		if university.courseExists(courseCode):
			
			newStudent = Student()
			newStudent.setID(str(baseID))
			newStudent.setCourse(courseCode)
			
			lName = input("Enter a Last name: ")
			newStudent.setLName(lName)
			fName = input("Enter a First name: ")
			newStudent.setFName(fName)
			degreeType = input("[U] Undergraduate / [P] Postgraduate: ")
			degreeType = validator.validateDegreeType(degreeType)
			newStudent.setDegreeType(degreeType)
			residencyType = input("[D] Domestic / [I] International: ")
			residencyType = validator.validateResidencyType(residencyType)
			newStudent.setResidencyType(residencyType)
			studyType = input("[F] Full-time / [P] Part-time: ")
			studyType = validator.validateStudyType(studyType)
			newStudent.setStudyType(studyType)
			
			course = university.courses[courseCode]
			course.addStudent(newStudent.ID)
			university.addStudent(newStudent)
			university.addCourse(course)
			
			print("\nSUCCESS: STUDENT RECORD CREATED")
			newStudent.displayDetails()
			return baseID + 1
		else:
			print("ERROR: Course code does not exist")
			return baseID
		print("\n \n \n")
	
	# - Search Student
	def searchStudent(self,university):
		print("\n \n \n")
		print("SEARCHING A STUDENT:")
		ID = input("Enter a Student ID: ")
		if university.studentExists(ID):
			student = university.students[ID]
			courseCode = student.getCourseCode()
			course = university.courses[courseCode]
			student.displayDetails()
			print("Studying:")
			course.displayDetails()
			print("Units enrolled in:")
			for code in student.units:
				unit = university.units[code]
				print("\n" + unit.title + " (" + unit.code + ")")
		else:
			print("ERROR: Student ID does not exist")
		print("\n \n \n")
			
		
	# - Enrol Student
	def enrolStudent(self,university):
		print("\n \n \n")
		print("ENROLLING A STUDENT IN A UNIT:")
		ID = input("Please enter the student ID of the student you wish to enroll: ")
		if university.studentExists(ID):
			code = input("Please enter the unit code of the unit you wish to enroll in: ")
			if university.unitExists(code):
				unit = university.units[code]
				student = university.students[ID]
				unit.addStudent(ID)
				student.addUnit(code)
				university.addUnit(unit)
				university.addStudent(student)
				print("\nSUCCESS: " + student.getName() + " enrolled in " + unit.getCode() + "(" + unit.getTitle() + ")")
			else:
				print("ERROR: Unit code does not exist")
		else:
			print("ERROR: Student ID does not exist")
		print("\n \n \n")
	
	# - Display Undergraduate Students
	def displayUndergraduateStudents(self,university):
		print("\n \n \n")
		print("DISPLAYING UNDERGRADUATE STUDENTS:")
		for ID, student in university.students.items():
			if student.degreeType == "U" or student.degreeType == "u":
				print(student.ID + " - " + student.getName())
		print("\n \n \n")
	
	# - Display Postgraduate Students
	def displayPostgraduateStudents(self,university):
		print("\n \n \n")
		print("DISPLAYING POSTGRADUATE STUDENTS:")
		for ID, student in university.students.items():
			if student.degreeType == "P" or student.degreeType == "p":
				print(student.ID + " - " + student.getName())
		print("\n \n \n")
	
	# - Display Domestic Students
	def displayDomesticStudents(self,university):
		print("\n \n \n")
		print("DISPLAYING DOMESTIC STUDENTS:")
		for ID, student in university.students.items():
			if student.residencyType == "D" or student.residencyType == "d":
				print(student.ID + " - " + student.getName())
		print("\n \n \n")
	
	# - Display International Students
	def displayInternationalStudents(self,university):
		print("\n \n \n")
		print("DISPLAYING INTERNATIONAL STUDENTS:")
		for ID, student in university.students.items():
			if student.residencyType == "I" or student.residencyType == "i":
				print(student.ID + " - " + student.getName())
		print("\n \n \n")
	
	# - Is Student enrolled in Unit?
	def checkUnitEnrolment(self,university):
		print("\n \n \n")
		print("CHECKING STUDENT ENROLMENT (UNIT):")
		ID = input("Enter a Student ID: ")
		if university.studentExists(ID):
			code = input("Enter a Unit code: ")
			if university.unitExists(code):
				student = university.students[ID]
				if code in student.units:
					print(student.getName + " is enrolled in " + code)
				else:
					print(student.getName + " has not been enrolled in " + code)
			else:
				print("ERROR: Unit code does not exist")
		else:
			print("ERROR: Student ID does not exist")
		print("\n \n \n")
	
	# - Is Student enrolled in Course?
	def checkCourseEnrolment(self,university):
		print("\n \n \n")
		print("CHECKING STUDENT ENROLMENT (COURSE):")
		ID = input("Enter a Student ID: ")
		if university.studentExists(ID):
			code = input("Enter a Course code: ")
			if university.courseExists(code):
				student = university.students[ID]
				if student.course == code:
					print(student.getName + " is enrolled in " + code)
				else:
					print(student.getName + " has not been enrolled in " + code)
			else:
				print("ERROR: Course code does not exist")
		else:
			print("ERROR: Student ID does not exist")
		print("\n \n \n")
	
	# - Edit Student Details
	def editStudentDetails(self, university):
		print("\n \n \n")
		print("EDITING STUDENT DETAILS:")
		ID = input("Enter a Student ID: ")
		if university.studentExists(ID):
			student = university.students[ID]
			courseCode = student.course
			
			university.students.pop(ID,None)
			newStudent = Student()
			newStudent.setID(ID)
			newStudent.setCourse(courseCode)
			
			lName = input("Enter a Last name: ")
			newStudent.setLName(lName)
			fName = input("Enter a First name: ")
			newStudent.setFName(fName)
			degreeType = input("[U] Undergraduate / [P] Postgraduate: ")
			degreeType = validator.validateDegreeType(degreeType)
			newStudent.setDegreeType(degreeType)
			residencyType = input("[D] Domestic / [I] International: ")
			residencyType = validator.validateResidencyType(residencyType)
			newStudent.setResidencyType(residencyType)
			studyType = input("[F] Full-time / [P] Part-time: ")
			studyType = validator.validateStudyType(studyType)
			newStudent.setStudyType(studyType)

			university.addStudent(newStudent)
			
			print("\nSUCCESS: STUDENT RECORD EDITED\n")
			newStudent.displayDetails()
		else:
			print("ERROR: Student ID does not exist")
		print("\n \n \n")
	
	# - Delete Student
	def deleteStudent(self,university):
		print("\n \n \n")
		print("REMOVING STUDENT FROM UNIVERSITY:")
		ID = input("Enter a Student ID: ")
		if university.studentExists(ID):
			student = university.students[ID]
			name = student.getName()
			university.students.pop(ID,None)
			print("\nSUCCESS:" + name + " has been removed from the system")
		else:
			print("ERROR: Student ID does not exist")
		print("\n \n \n")
	
	
	# COURSE METHODS
	
	# - Create Course
	def createCourse(self,university):
		print("\n \n \n")
		print("CREATING A COURSE:")
		newCourse = Course()
		code = input("Enter a Course code: ")
		code = validator.validateCourseCode(code)
		newCourse.setCode(code)
		name = input("Enter a Course name: ")
		newCourse.setName(name)
		university.addCourse(newCourse)
		print("\nSUCCESS: COURSE RECORD CREATED\n")
		newCourse.displayDetails()
		print("\n \n \n")
	
	# - Search Course
	def searchCourse(self,university):
		print("\n \n \n")
		print("SEARCHING A COURSE:")
		code = input("Enter a Course code: ")
		if university.courseExists(code):
			course = university.courses[code]
			course.displayDetails()
		else:
			print("ERROR: Course code does not exist")
		print("\n \n \n")
		
	# - Display All Courses
	def displayAllCourses(self,university):
		print("\n \n \n")
		print("DISPLAYING ALL COURSES:")
		university.displayCourses()
		print("\n \n \n")
	
	# - Display Units in Course
	def displayUnitsInCourse(self,university):
		print("\n \n \n")
		print("DISPLAYING ALL UNITS IN A COURSE:")
		courseCode = input("Enter a Course code: ")
		if university.courseExists(courseCode):
			course = university.courses[courseCode]
			for code in course.units:
				unit = university.units[code]
				print("\n" + unit.title + " - " + unit.code)
		else:
			print("ERROR: Course code does not exist")
		print("\n \n \n")
	
	# - Edit Course Details
	def editCourseDetails(self,university):
		print("\n \n \n")
		print("EDITING COURSE DETAILS:")
		code = input("Enter a Course code: ")
		if university.courseExists(code):
			university.courses.pop(code,None)
			newCourse = Course()
			code = input("Enter a Course code: ")
			code = validator.validateCourseCode(code)
			newCourse.setCode(code)
			name = input("Enter a Course name: ")
			newCourse.setName(name)
			university.addCourse(newCourse)
			print("\nSUCCESS: COURSE RECORD EDITED")
			newCourse.displayDetails()
		else:
			print("ERROR: Course code does not exist")
		print("\n \n \n")
	
	# - Delete Course
	def deleteCourse(self,university):
		print("\n \n \n")
		print("DELETING A COURSE:")
		code = input("Enter a Course code: ")
		if university.courseExists(code):
			course = university.courses[code]
			name = course.name
			university.courses.pop(code,None)
			print("\nSUCCESS: " + name + " has been deleted")
		else:
			print("ERROR: Course code does not exist")
		print("\n \n \n")