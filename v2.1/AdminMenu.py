from CourseAdmin import CourseAdmin
from University import University
from Course import Course
from Unit import Unit
from Student import Student

# Initialise global variables
def main():
	baseID = 10000000
	CA = CourseAdmin()
	Monash = University("Monash University")
	mainMenu()
	print("hi")
	
# Top level menu (z-index: 5)
def mainMenu():
	print("\n" +
	"Welcome!" +
	"\n [1] Courses" + 
	"\n [2] Units" +
	"\n [3] Students" +
	"\n [4] Quit"
	)
	command = input("Please select a number from above")