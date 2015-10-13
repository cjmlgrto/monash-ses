__author__ = 'xav_work'

from CourseAdmin import CourseAdmin
from Student import Student
from Unit import Unit
from Course import Course
from University import University

'''
UNFINISHED - NEEDS LOTS OF WORK BUT IT SEEMS THAT WE ONLY NEED TO FOCUS ON the 4 use cases given for week 11, will come
back to it when have time.
'''


def main():
    quit = False
    adminMenu = str("\n Please select from the following options: " + "\n [1] Create a new student"
    + "\n [2] Create a new Unit" + "\n [3] Create a new Course" + "\n [4] Enroll a student"
    + "\n [5] Search student in Unit" + "\n [6] Search student in Course" + "\n [7] Re-print menu"
    + "\n [8] Quit" )

    sesStartup = str('''
-----------------------------------------------------------------------------------------------------------------------

 .----------------.  .----------------.  .-----------------. .----------------.  .----------------..----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |     ____     | || | ____  _____  | || |      __      | || |    _______   | || |  ____  ____  | |
| ||_   \  /   _|| || |   .'    `.   | || ||_   \|_   _| | || |     /  \     | || |   /  ___  |  | || | |_   ||   _| | |
| |  |   \/   |  | || |  /  .--.  \  | || |  |   \ | |   | || |    / /\ \    | || |  |  (__ \_|  | || |   | |__| |   | |
| |  | |\  /| |  | || |  | |    | |  | || |  | |\ \| |   | || |   / ____ \   | || |   '.___`-.   | || |   |  __  |   | |
| | _| |_\/_| |_ | || |  \  `--'  /  | || | _| |_\   |_  | || | _/ /    \ \_ | || |  |`\____) |  | || |  _| |  | |_  | |
| ||_____||_____|| || |   `.____.'   | || ||_____|\____| | || ||____|  |____|| || |  |_______.'  | || | |____||____| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |  PROPERTY OF MONASH UNIVERSITY
| |    _______   | || |  _________   | || |    _______   | |  CREATED USING RESOURCES OF FIT1010
| |   /  ___  |  | || | |_   ___  |  | || |   /  ___  |  | |  AUTHORS:
| |  |  (__ \_|  | || |   | |_  \_|  | || |  |  (__ \_|  | |  CARLOS MELEGRITO & JOSH NELSSON-SMITH
| |   '.___`-.   | || |   |  _|  _   | || |   '.___`-.   | |
| |  |`\____) |  | || |  _| |___/ |  | || |  |`\____) |  | |
| |  |_______.'  | || | |_________|  | || |  |_______.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'

 -----------------------------------------------------------------------------------------------------------------------''')
    CA = CourseAdmin()
    print(sesStartup)
    studID = 10000000
    while not quit:
        print(adminMenu)
        validInput = False
        while not validInput:
            try:
                num1 = input('\nEnter: ')
                if int(num1) <= 8 and int(num1) >= 1:
                    validInput = True
                    num1 = int(num1)

                    if num1 == 1:
                        hello = CA.createStudent(studID)
                        studID += 1

                    if num1 == 2:
                        pass

                    if num1 == 3:
                        pass

                    if num1 == 4:
                        pass

                    if num1 == 5:
                        pass

                    if num1 == 6:
                        pass

                    if num1 == 7:
                        pass

                    if num1 == 8:
                        quit = True
                        print("Thankyou, see you later :)")
                else:
                    raise ValueError
            except ValueError:
                print("\nError: Please enter a number between 1 and 8")


if __name__ == "__main__":
    main()