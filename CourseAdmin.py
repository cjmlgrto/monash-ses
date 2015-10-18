# AdminMenu
# - The interface for the Monash SES
# - Main functionality is to display a list of options and then run the commands

# Class Dependencies: 
# - sys, (~/dev)
# - Enrolment, (Enrolment.py)
# - University, (University.py)
# - Course, (Course.py)
# - Unit, (Unit.py)
# - Student, (Student.py)
# - Validate, (Validate.py)

import sys
from Enrolment import Enrolment
from University import University
from menuValidation import promptCommand


# INITIALISE GLOBAL VARIABLES
# - baseID, the first iteration of the student count
# - admin, a new Enrolment instance
# - monash, a new University instance

global baseID
baseID = 10000000
admin = Enrolment()
monash = University("Monash University")

def main():
	str = '''
8b    d8  dP"Yb  88b 88    db    .dP"Y8 88  88    .dP"Y8 888888 .dP"Y8 
88b  d88 dP   Yb 88Yb88   dPYb   `Ybo." 88  88    `Ybo." 88__   `Ybo." 
88YbdP88 Yb   dP 88 Y88  dP__Yb  o.`Y8b 888888    o.`Y8b 88""   o.`Y8b 
88 YY 88  YbodP  88  Y8 dP""""Yb 8bodP' 88  88    8bodP' 888888 8bodP'

 ~~ PROPERTY OF MONASH UNIVERSITY, CREATED WITH FIT1010 RESOURCES ~~
      ~~ DEVELOPED BY JOSH NELSSON-SMITH & CARLOS MELEGRITO ~~

	'''
	print(str)
	mainMenu(baseID)

def mainMenu(baseID):
	print("---------------------------------------------------------------------")
	print("\nWELCOME, COURSE ADMIN!" +
	"\n" +
	"\n [1] Courses Menu" + 
	"\n [2] Units Menu" +
	"\n [3] Students Menu" +
	"\n [4] Quit"
	)
	command = promptCommand(1,4)
	if int(command) == 1:
		coursesMenu()
	if int(command) == 2:
		unitsMenu()
	if int(command) == 3:
		studentsMenu(baseID)
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
	"\n [7] Display students in course with filter" +
	"\n [8] Back to Main Menu"
	)
	command = promptCommand(1,8)
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
		admin.displayFilterStudentsInCourse(monash)
		coursesMenu()
	if int(command) == 8:
		mainMenu(baseID)
	
def unitsMenu():
	print("\nUNITS OPTIONS" +
	"\n" +
	"\n [1] Create Unit" + 
	"\n [2] Search Unit" +
	"\n [3] Display All Units" +
	"\n [4] Display Students in Unit" +
	"\n [5] Edit Unit Details" +
	"\n [6] Delete Unit" +
	"\n [7] Filter Search students in unit"
	"\n [8] Back to Main Menu"
	)
	command = promptCommand(1,8)
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
		admin.displayFilterStudentsInUnit(monash)
		unitsMenu()
	if int(command) == 8:
		mainMenu(baseID)
	
def studentsMenu(baseID):
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
		nunv = admin.createStudent(baseID,monash)
		baseID = nunv
		# input("Hit enter to return to menu")
		studentsMenu(baseID)
	if int(command) == 2:
		admin.searchStudent(monash)
		studentsMenu(baseID)
	if int(command) == 3:
		admin.enrolStudent(monash)
		studentsMenu(baseID)
	if int(command) == 4:
		admin.displayUndergraduateStudents(monash)
		studentsMenu(baseID)
	if int(command) == 5:
		admin.displayPostgraduateStudents(monash)
		studentsMenu(baseID)
	if int(command) == 6:
		admin.displayDomesticStudents(monash)
		studentsMenu(baseID)
	if int(command) == 7:
		admin.displayInternationalStudents(monash)
		studentsMenu(baseID)
	if int(command) == 8:
		admin.checkUnitEnrolment(monash)
		studentsMenu(baseID)
	if int(command) == 9:
		admin.checkCourseEnrolment(monash)
		studentsMenu(baseID)
	if int(command) == 10:
		admin.editStudentDetails(monash)
		studentsMenu(baseID)
	if int(command) == 11:
		admin.deleteStudent(monash)
		studentsMenu(baseID)
	if int(command) == 12:
		mainMenu(baseID)
	

	

# Run on startup	
if __name__ == "__main__":
    main()

