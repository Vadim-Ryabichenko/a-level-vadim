import sys, os
import csv
parent_dir = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..'))
sys.path.append(parent_dir)
from unittest import TestCase
from OOP.employee18 import Employee, EmailAlreadyExistsException


class EmployeeTest(TestCase):

    def setUp(self):
        self.emp = Employee(name="Roma", job_title="Employee", salary_day=45, email="rrsrsoma@gmail.com")
        self.emp2 = Employee(name="Vika", job_title="Employee", salary_day=35, email="kssrkkol@gmail.com")

    def test_str(self):
        self.assertEqual(self.emp.__str__(), "Employee : Roma")

    def test_work(self):
        self.assertEqual(self.emp.work(), "I come to the office.")

    def test_gt(self):
        self.assertEqual(self.emp > self.emp2, True)

    def test_check_salary(self):
        self.assertEqual(self.emp.check_salary(14), "Salary for 14 days = 450 dollars")

    def test_save_email(self):
        self.emp.save_email(self.emp.email)
        with open("test_emails.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                saved_email = row[-1]
        self.assertEqual(saved_email, "kssrkkol@gmail.com")

    def test_validate(self):
        email = "kssrkkol@gmail.com"
        with self.assertRaises(EmailAlreadyExistsException) as context:
            self.emp2.validate(email)
        self.assertEqual(str(context.exception), f"email {email} already exist in emails.csv")










