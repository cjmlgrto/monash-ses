# Validate CLASS
# - Module for validation

# Class Dependencies: 
# - re, regular expressions are used for validation purposes

# Attributes: 
# - n/a

import re

class Validate:
	
	def validateUnitCode(self,unitCode):
		matchObject = re.match(r'^[A-Z]{3}[0-9]{4}$',unitCode, re.I)  # matches a unitCode of form ABC1234
		if matchObject:
			return True, str(matchObject.group()).upper()
		else:
			return False, None
		
	def validateDegreeType(self,degreeType):
		matchObject = re.match(r'^[U,P]$', degreeType, re.I)
		if matchObject:
			return True, str(matchObject.group().upper())
		else:
			return False, None
		
	def validateResidencyType(self,residencyType):
		matchObject = re.match(r'^[D,I]$', residencyType, re.I)
		if matchObject:
			return True, str(matchObject.group().upper())
		else:
			return False, None
		
	def validateStudyType(self,studyType):
		matchObject = re.match(r'^[F,P]$', studyType, re.I)
		if matchObject:
			return True, str(matchObject.group().upper())
		else:
			return False, None
		
	def validateCourseCode(self,courseCode):
		matchObject = re.match(r'^[A-Z]{0,1}[0-9]{4}$', courseCode, re.I) # matches traditional courseCode 1234 or new A1234
		if matchObject:
			return True, str(matchObject.group()).upper()
		else:
			return False, None

	def validateStudentID(self, studID):
		matchObject = re.match(r'^[1-9][0-9]{7}$', studID) # matches a stud ID starting with 1-9 and having 8 total numbers
		if matchObject:
			return True, str(matchObject.group())
		else:
			return False, None
