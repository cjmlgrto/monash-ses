__author__ = 'Josh'

import unittest
from Unit import Unit

class UnitClassUnitTest(unittest.TestCase):

    '''
    def setUp(self):
        self.unit = Unit()
        self.file = open("filedirect", "r")

    def tearDown(self):
        self.file.close()
    '''

    def setUp(self):
        self.unit = Unit()


    def testA(self):
        self.unit.setCode('FIT1004')
        assert self.unit.code == 'FIT1004', "setCode not functioning correctly"

    def testB(self):
        self.unit.setTitle('Databases')
        assert self.unit.title == 'Databases', "setTitle not functioning correctly"

    def testC(self):
        self.unit.addCourse('2770')
        assert '2770' in self.unit.courses, "course code not being added correctly"

    def testD(self):
        self.unit.addStudent('10000000')
        assert '10000000' in self.unit.students, "student ID not being added correctly"

    def testE(self):
        self.unit.code = 'FIT1004'
        assert self.unit.getCode() == 'FIT1004', "correct unit code isn't being returned"

    def testF(self):
        self.unit.title = 'Databases'
        assert self.unit.getTitle() == 'Databases', "correct title not being returned"

if __name__ == "__main__":
    unittest.main()