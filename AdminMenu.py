# AdminMenu
# - The interface for the Monash SES

# Class Dependencies: 
# - sys, (~/dev)
# - CourseAdmin, (CourseAdmin.py)
# - University, (University.py)
# - Course, (Course.py)
# - Unit, (Unit.py)
# - Student, (Student.py)
# - Validate, (Validate.py)

import sys
from CourseAdmin import CourseAdmin
from University import University
from Course import Course
from Unit import Unit
from Student import Student

# INITIALISE GLOBAL VARIABLES
# - baseID, the first iteration of the student count
# - admin, a new CourseAdmin instance
# - monash, a new University instance

baseID = 10000000
admin = CourseAdmin()
monash = University("Monash University")

def main():
	mainMenu()

def mainMenu():
	print("\nWELCOME, COURSE ADMIN!" +
	"\n" +
	"\n [1] Courses" + 
	"\n [2] Units" +
	"\n [3] Students" +
	"\n [4] Quit"
	)
	command = promptCommand(1,4)
	if int(command) == 1:
		coursesMenu()
	if int(command) == 2:
		unitsMenu()
	if int(command) == 3:
		studentsMenu()
	if int(command) == 4:
		sys.exit(0)
	
def coursesMenu():
	print("\nCOURSES OPTIONS" +
	"\n" +
	"\n [1] Create Course" + 
	"\n [2] Search Course" +
	"\n [3] Display All Courses" +
	"\n [4] Display Units in Course" +
	"\n [5] Edit Course Details" +
	"\n [6] Delete Course" +
	"\n [7] Back to Main Menu"
	)
	command = promptCommand(1,7)
	if int(command) == 1:
		admin.createCourse(monash)
		coursesMenu()
	if int(command) == 2:
		admin.searchCourse(monash)
		coursesMenu()
	if int(command) == 3:
		admin.displayAllCourses(monash)
		coursesMenu()
	if int(command) == 4:
		admin.displayUnitsInCourse(monash)
		coursesMenu()
	if int(command) == 5:
		admin.editCourseDetails(monash)
		coursesMenu()
	if int(command) == 6:
		admin.deleteCourse(monash)
		coursesMenu()
	if int(command) == 7:
		mainMenu()
	
def unitsMenu():
	print("\nUNITS OPTIONS" +
	"\n" +
	"\n [1] Create Unit" + 
	"\n [2] Search Unit" +
	"\n [3] Display All Units" +
	"\n [4] Display Students in Unit" +
	"\n [5] Edit Unit Details" +
	"\n [6] Delete Unit" +
	"\n [7] Back to Main Menu"
	)
	command = promptCommand(1,7)
	if int(command) == 1:
		admin.createUnit(monash)
		unitsMenu()
	if int(command) == 2:
		admin.searchUnit(monash)
		unitsMenu()
	if int(command) == 3:
		admin.displayAllUnits(monash)
		unitsMenu()
	if int(command) == 4:
		admin.displayStudentsInUnit(monash)
		unitsMenu()
	if int(command) == 5:
		admin.editUnitDetails(monash)
		unitsMenu()
	if int(command) == 6:
		admin.deleteUnit(monash)
		unitsMenu()
	if int(command) == 7:
		mainMenu()
	
def studentsMenu():
	print("\nSTUDENTS OPTIONS" +
	"\n" +
	"\n [1] Create Student" + 
	"\n [2] Search Student" +
	"\n [3] Enrol Student" +
	"\n [4] Display Undergraduate Students" +
	"\n [5] Display Postgraduate Students" +
	"\n [6] Display Domestic Students" +
	"\n [7] Display International Students" +
	"\n [8] Is Student enrolled in Unit?" +
	"\n [9] Is Student enrolled in Course?" +
	"\n [10] Edit Student Details" +
	"\n [11] Delete Student" +
	"\n [12] Back to Main Menu"
	)
	command = promptCommand(1,12)
	if int(command) == 1:
		admin.createStudent(baseID,monash)
		# input("Hit enter to return to menu")
		studentsMenu()
	if int(command) == 2:
		admin.searchStudent(monash)
		studentsMenu()
	if int(command) == 3:
		admin.enrolStudent(monash)
		studentsMenu()
	if int(command) == 4:
		admin.displayUndergraduateStudents(monash)
		studentsMenu()
	if int(command) == 5:
		admin.displayPostgraduateStudents(monash)
		studentsMenu()
	if int(command) == 6:
		admin.displayDomesticStudents(monash)
		studentsMenu()
	if int(command) == 7:
		admin.displayInternationalStudents(monash)
		studentsMenu()
	if int(command) == 8:
		admin.checkUnitEnrolment(monash)
		studentsMenu()
	if int(command) == 9:
		admin.checkCourseEnrolment(monash)
		studentsMenu()
	if int(command) == 10:
		admin.editStudentDetails(monash)
		studentsMenu()
	if int(command) == 11:
		admin.deleteStudent(monash)
		studentsMenu()
	if int(command) == 12:
		mainMenu()
	
def promptCommand(lowest,highest):
	valid = False
	while not valid:
		command = input("\nEnter a number to choose from above: ")
		if command != "" and int(command) >= lowest and int(command) <= highest:
			return command
			valid = True
		else:
			print("\nError! Please try again.")
	

# Run on startup	
if __name__ == "__main__":
    main()