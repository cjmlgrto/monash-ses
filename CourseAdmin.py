from University import University
from Course import Course
from Unit import Unit
from Student import Student

class CourseAdmin:
	
	# UNIT METHODS
	
	# - Create Unit
	def createUnit(self,university):
		newUnit = Unit()
		code = input("New unit code: ")
		# validate
		newUnit.setCode(code)
		title = input("New unit title: ")
		# validate
		newUnit.setTitle(title)
		university.addUnit(newUnit)
		print("SUCCESS: UNIT RECORD CREATED")
		newUnit.displayDetails()
	
	# - Search Unit
	def searchUnit(self,university):
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
			
	# - Display All Units
	def displayAllUnits(self,university):
		university.displayUnits()
		
	# - Display Students in Unit
	def displayStudentsInUnit(self,university):
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			unit = university.units[code]
			print(unit.title + " has " + len(unit.students) + " students:")
			for ID in unit.students:
				student = university.students[ID]
				print("\n" + student.fName + " " + student.lName + " (" + student.ID + ")")
		else:
			print("ERROR: Unit code does not exist")
			
	# - Edit Unit Details
	def editUnitDetails(self,university):
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			university.units.pop(code, None)
			newUnit = Unit()
			code = input("New unit code: ")
			# validate
			newUnit.setCode(code)
			title = input("New unit title: ")
			# validate
			newUnit.setTitle(title)
			university.addUnit(newUnit)
			print("SUCCESS: UNIT RECORD CREATED")
			newUnit.displayDetails()
		else:
			print("ERROR: Unit code does not exist")
	
	# - Delete Unit
	def deleteUnit(self,university):
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			unit = university.units[code]
			title = unit.title
			university.units.pop(code, None)
			print("SUCCESS: " + title + " has been deleted")
		else:
			print("ERROR: Unit code does not exist")
	
	# STUDENT METHODS
	
	# - Create Student
	def createStudent(self,baseID,university):
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
			newStudent.setDegreeType(degreeType)
			residencyType = input("[D] Domestic / [I] International: ")
			newStudent.setResidencyType(residencyType)
			studyType = input("[F] Full-time / [P] Part-time: ")
			newStudent.setStudyType(studyType)
			
			course = university.courses[courseCode]
			course.addStudent(newStudent.ID)
			university.addStudent(newStudent)
			university.addCourse(course)
			
			print("SUCCESS: STUDENT RECORD CREATED")
			newStudent.displayDetails()
			return baseID + 1
		else:
			print("ERROR: Course code does not exist")
			return baseID
	
	# - Search Student
	def searchStudent(self,university):
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
			
		
	# - Enrol Student
	def enrolStudent(self,university):
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
				print("SUCCESS: " + student.getName() + " enrolled in " + unit.getCode() + "(" + unit.getTitle() + ")")
			else:
				print("ERROR: Unit code does not exist")
		else:
			print("ERROR: Student ID does not exist")
	
	# - Display Undergraduate Students
	def displayUndergraduateStudents(self,university):
		for ID, student in university.students.items():
			if student.degreeType == "U" or student.degreeType == "u":
				print(student.ID + " - " + student.getName())
		
	
	# - Display Postgraduate Students
	def displayPostgraduateStudents(self,university):
		for ID, student in university.students.items():
			if student.degreeType == "P" or student.degreeType == "p":
				print(student.ID + " - " + student.getName())
	
	# - Display Domestic Students
	def displayDomesticStudents(self,university):
		for ID, student in university.students.items():
			if student.residencyType == "D" or student.residencyType == "d":
				print(student.ID + " - " + student.getName())
	
	# - Display International Students
	def displayInternationalStudents(self,university):
		for ID, student in university.students.items():
			if student.residencyType == "I" or student.residencyType == "i":
				print(student.ID + " - " + student.getName())
	
	# - Is Student enrolled in Unit?
	def checkUnitEnrolment(self,university):
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
	
	# - Is Student enrolled in Course?
	def checkCourseEnrolment(self,university):
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
	
	# - Edit Student Details
	def editStudentDetails(self, university):
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
			newStudent.setDegreeType(degreeType)
			residencyType = input("[D] Domestic / [I] International: ")
			newStudent.setResidencyType(residencyType)
			studyType = input("[F] Full-time / [P] Part-time: ")
			newStudent.setStudyType(studyType)

			university.addStudent(newStudent)
			
			print("SUCCESS: STUDENT RECORD EDITED")
			newStudent.displayDetails()
		else:
			print("ERROR: Student ID does not exist")
	
	# - Delete Student
	def deleteStudent(self,university):
		ID = input("Enter a Student ID: ")
		if university.studentExists(ID):
			student = university.students[ID]
			name = student.getName()
			university.students.pop(ID,None)
			print("SUCCESS:" + name + " has been removed from the system")
		else:
			print("ERROR: Student ID does not exist")
	
	
	# COURSE METHODS
	
	# - Create Course
	def createCourse(self,university):
		newCourse = Course()
		code = input("Enter a Course code: ")
		# validate
		newCourse.setCode(code)
		name = input("Enter a Course name: ")
		# validate
		newCourse.setName(name)
		university.addCourse(newCourse)
		print("SUCCESS: COURSE RECORD CREATED")
		newCourse.displayDetails()
	
	# - Search Course
	def searchCourse(self,university):
		code = input("Enter a Course code: ")
		if university.courseExists(code):
			course = university.courses[code]
			course.displayDetails()
		else:
			print("ERROR: Course code does not exist")
		
	# - Display All Courses
	def displayAllCourses(self,university):
		university.displayCourses()
	
	# - Display Units in Course
	def displayUnitsInCourse(self,university):
		courseCode = input("Enter a Course code: ")
		if university.courseExists(courseCode):
			course = university.courses[courseCode]
			for code in course.units:
				unit = university.units[code]
				print("\n" + unit.title + " - " + unit.code)
		else:
			print("ERROR: Course code does not exist")
	
	# - Edit Course Details
	def editCourseDetails(self,university):
		code = input("Enter a Course code: ")
		if university.courseExists(code):
			university.courses.pop(code,None)
			newCourse = Course()
			code = input("Enter a Course code: ")
			# validate
			newCourse.setCode(code)
			name = input("Enter a Course name: ")
			# validate
			newCourse.setName(name)
			university.addCourse(newCourse)
			print("SUCCESS: COURSE RECORD EDITED")
			newCourse.displayDetails()
		else:
			print("ERROR: Course code does not exist")
	
	# - Delete Course
	def deleteCourse(self,university):
		code = input("Enter a Course code: ")
		if university.courseExists(code):
			course = university.courses[code]
			name = course.name
			university.courses.pop(code,None)
			print("SUCCESS: " + name + " has been deleted")
		else:
			print("ERROR: Course code does not exist")