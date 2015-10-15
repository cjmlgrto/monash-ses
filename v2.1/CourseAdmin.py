from University import University
from Course import Course
from Unit import Unit
from Student import Student

class CourseAdmin:
	
	# UNIT METHODS
	
	# - Create Unit
	
	# - Search Unit
	
	# - Display All Units
	
	# - Display Students in Unit
	
	# - Edit Unit Details
	
	# - Delete Unit
	
	
	# STUDENT METHODS
	
	# - Create Student
	def createStudent(self,baseID,university):
		courseCode = input("Please enter the code for the Course the student is enrolled in: ")
		if university.courseExists(courseCode):
			newStudent = Student()
			newStudent.setID(str(baseID))
			newStudent.setCourseCode(courseCode)
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
			print("\n" +
			"SUCCESS: STUDENT RECORD CREATED"
			)
			print("\n" +
			newStudent.displayDetails()
			)
			return baseID + 1
		else:
			print("\n" +
			"ERROR: Course code does not exist"
			)
			return baseID
	
	# - Search Student
	
	# - Enrol Student
	
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
	
	# - Search Course
	
	# - Display All Courses
	
	# - Display Units in Course
	
	# - Edit Course Details
	
	# - Delete Course