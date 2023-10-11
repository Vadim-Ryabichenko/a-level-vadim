import sys, os
parent_dir = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..'))
sys.path.append(parent_dir)
from unittest import TestCase
from OOP.employee18 import Recruiter


class RecruiterTest(TestCase):

    def setUp(self):
        self.rec = Recruiter(name="Tom", job_title="Recruiter", salary_day=20, email="tommy@gmail.com")
        self.rec2 = Recruiter(name="Jerry", job_title="Recruiter", salary_day=26, email="jerry@gmail.com")

    def test_work(self):
        self.assertEqual(self.rec.work(), "I come to the office and start to hiring.")