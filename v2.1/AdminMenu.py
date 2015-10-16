from CourseAdmin import CourseAdmin
from University import University
from Course import Course
from Unit import Unit
from Student import Student

def main():
	baseID = 10000000
	CA = CourseAdmin()
	Monash = University("Monash University")
	mainMenu()
	
def mainMenu():
	print("\n" +
	"Welcome!" +
	"\n [1] Courses" + 
	"\n [2] Units" +
	"\n [3] Students" +
	"\n [4] Quit"
	)
	
def coursesMenu():
	print("\n" +
	"COURSES OPTIONS" +
	"\n [1] Create Course" + 
	"\n [2] Search Course" +
	"\n [3] Display All Courses" +
	"\n [4] Display Units in Course" +
	"\n [5] Edit Course Details" +
	"\n [6] Delete Course" +
	"\n [7] Back to Main Menu"
	)
	
def unitsMenu():
	print("\n" +
	"UNITS OPTIONS" +
	"\n [1] Create Unit" + 
	"\n [2] Search Unit" +
	"\n [3] Display All Units" +
	"\n [4] Display Students in Unit" +
	"\n [5] Edit Unit Details" +
	"\n [6] Delete Unit" +
	"\n [7] Back to Main Menu"
	)
	
def studentsMenu():
	print("\n" +
	"STUDENTS OPTIONS" +
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
	

# Run on startup	
if __name__ == "__main__":
    main()