# Monash SES II

![Screen shot here](https://raw.githubusercontent.com/cjmlgrto/MonashSES/master/screenshot.png)

## About

This project is an assessment task for Monash University’s Introduction to Software Engineering (FIT1010) unit. SES stands for “Student Enrolment System”, a command-line interface designed to simulate the administration and management of students, units and courses within a university. 

The goal of this project is to understand good software engineering practices under the Unified Process, and to better understand the Object-Oriented Programming paradigm.

All rights reserved by Monash University’s Faculty of IT. Created under their resources, developed and designed by Josh Nelsson-Smith and CJ Melegrito.

## Quick-Start Guide

To start, run “CourseAdmin.py” in a python-enabled command line interface. If you’re using SHELL, open folder these files are located in, and run:

	python3 CourseAdmin.py

## The 6 Main Use-Cases

### Create Course

Before you begin, a course needs to be created. To do this, go to **Main Menu** → **Courses Menu** → **Create Course** and follow the prompts.

### Create Unit

To create a new unit, under the **Main Menu**, go to **Units Menu** → **Create Unit**, and follow the prompts.

### Create Student

To add a student to the university system, under the **Main Menu**, go to **Students Menu** → **Create Student**, and follow the prompts as necessary. (Note: a course must have already been created before adding a student to the university system).

### Enroll Student

Under the **Main Menu**, go to **Students Menu** → **Enroll Student**, and follow the prompts as needed.

### Display Student Information (Within Unit)

In the **Main Menu** go to the **Units Menu** → **Filter Search students in unit**. Here, you can select to see undergraduate/postgraduate students, international/domestic students and full-time/part-time students *within a particular **unit***.

### Display Student Information (Within Course)

In the **Main Menu** go to the **Courses Menu** → **Filter Search students in unit**. Here, you can select to see undergraduate/postgraduate students, international/domestic students and full-time/part-time students *within a particular **course***.

## Files Included

- `CourseAdmin.py`, the main file that presents the command-line interface onscreen options
- `Enrolment.py`, contains all the methods required to complete tasks in the SES
- `Validate.py`, a module used to validate user input
- `menuValidation.py`, a module used to navigate the command-line interface
- `University.py`, the University class that contains the database of students, units and courses
- `Courses.py`, the Course class that initialises for every new instance of a course object
- `Units.py`, the Unit class that initialises for every new instance of a unit object
- `Student.py`, the Student class that initialises for every new instance of a student object

