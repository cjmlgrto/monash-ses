from University import University
from Course import Course
from Unit import Unit
from Student import Student

class CourseAdmin:
	
	# UNIT METHODS
	
	# - Create Unit
	def createUnit(self,university):
		newUnit = Unit()
		code = input("Please enter Unit code: ")
		# validate
		newUnit.setCode(code)
		title = input("Please enter Unit title: ")
		# validate
		newUnit.setTitle(title)
		university.addUnit(newUnit)
		print("SUCCESS: UNIT RECORD CREATED")
		print("\n" +
		newUnit.displayDetails()
		)
	
	# - Search Unit
	def searchUnit(self,university):
		code = input("Enter a Unit code: ")
		if university.unitExists(code):
			unit = university.units[code]
			print("\n" +
			unit.displayDetails()
			)
			# iterate over each student enrolled
			print("\n" +
			"Students enrolled in this unit:"
			)
			for ID in unit.studentList:
				student = university.students[ID]
				print("\n" + student.fName + " " + student.lName + " (" + student.ID + ")")
		else:
			print("ERROR: Unit code does not exist")
	# - Display All Units
	
	# - Display Students in Unit
	
	# - Edit Unit Details
	
	# - Delete Unit
	
	
	# STUDENT METHODS
	
	# - Create Student
	def createStudent(self,baseID,university):
		courseCode = input("Please enter a course code: ")
		if university.courseExists(courseCode):
			newStudent = Student()
			newStudent.setID(str(baseID))
			newStudent.setCourseCode(courseCode)
			# let the input begin
			lName = input("Please enter the student's last name: ")
			newStudent.setLName(lName)
			fName = input("Please enter the student's last name: ")
			newStudent.setFName(fName)
			degreeType = input("Please enter the student's degree type (U for undergraduate or P for postgraduate): ")
			# validate
			newStudent.setDegreeType(degreeType)
			residencyType = input("Please enter the student's residency type (I for International, or D for Domestic):  ")
			# validate
			newStudent.setResidencyType(residencyType)
			# validate
			studyType = input("Please enter the student's study type (F for full time, P for part time): ")
			newStudent.setStudyType(studyType)
			university.addStudent(newStudent)
			print("SUCCESS: STUDENT RECORD CREATED")
			print("\n" +
			newStudent.displayDetails()
			)
			# increment student count / student ID by 1 per new student created
			return baseID + 1
		else:
			print("ERROR: Course code does not exist")
			return baseID
	
	# - Search Student
	def searchStudent(self,university):
		ID = input("Please enter the student ID of the student you wish to display details of: ")
		if university.studentExists(ID):
			student = university.students[ID]
			courseCode = student.getCourseCode()
			course = university.courses[courseCode]
			print("\n" +
			student.displayDetails()
			)
			print("\n" +
			"Studying: " + course.displayDetails()
			)
			# iterate over student's units and print them out neatly
			print("\n" + "Units enrolled in:")
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
				# merge back into University database
				university.addUnit(unit)
				university.addStudent(student)
				print("SUCCESS: " + student.getName() + " enrolled in " + unit.getCode() + "(" + unit.getTitle() + ")")
			else:
				print("ERROR: Unit code does not exist")
		else:
			print("ERROR: Student ID does not exist")
	
	# - Display Undergraduate Students
	
	# - Display Postgraduate Students
	
	# - Display Domestic Students
	
	# - Display International Students
	
	# - Is Student enrolled in Unit?
	
	# - Is Student enrolled in Course?
	
	# - Edit Student Details
	
	# - Delete Student
	
	
	# COURSE METHODS
	
	# - Create Course
	def createCourse(self,university):
		newCourse = Course()
		code = input("Please enter Course Code: ")
		# validate
		newCourse.setCode(code)
		name = input("Please enter Course Name: ")
		# validate
		newCourse.setName(name)
		university.addCourse(newCourse)
		print("SUCCESS: COURSE RECORD CREATED")
		print("\n" +
		newCourse.displayDetails()
		)
	
	# - Search Course
	def searchCourse(self,university):
		code = input("Please enter a course code")
		if university.courseExists(code):
			course = university.course[code]
			print("\n" +
			course.displayDetails()
			)
			""
		
	# - Display All Courses
	
	# - Display Units in Course
	
	# - Edit Course Details
	
	# - Delete Course