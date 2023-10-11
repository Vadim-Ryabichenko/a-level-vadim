import sys, os
parent_dir = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..'))
sys.path.append(parent_dir)
from unittest import TestCase
from OOP.employee18 import Developer

class DeveloperTest(TestCase):

    def setUp(self):
        self.dev = Developer(name="Nona", job_title="Developer", salary_day=60, tech_stack=["django", "selenium", "sql"], email="nfoаffefffhftogfkaf@gmail.com")
        self.dev2 = Developer(name="John", job_title="Developer", salary_day=65, tech_stack=["django", "react", "mysql", "postgresql"], email="hyаfffkogfeffkhfftyyyy@gmail.com")

    def test_work(self):
        self.assertEqual(self.dev.work(), "I come to the office and start to coding.")

    def test_gt(self):
        self.assertEqual(self.dev > self.dev2, False)

    def test_combined_bigger_salary(self):
        self.assertEqual(self.dev.combined_bigger_salary(self.dev2), self.dev2.salary_for_day)

    def test_add(self):
        self.assertEqual((self.dev + self.dev2).__str__(), "Developer : Nona John")
