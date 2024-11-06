# test person
import unittest

from project.employee import Employee
from project.person import Person
from project.teacher import Teacher


class Tests(unittest.TestCase):
    def test_person(self):
        p = Person()
        res = p.sleep()
        self.assertEqual(res, "sleeping...")

    def test_empl(self):
        p = Employee()
        res = p.get_fired()
        self.assertEqual(res, "fired...")