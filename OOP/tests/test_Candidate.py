import sys, os
parent_dir = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..'))
sys.path.append(parent_dir)
from unittest import TestCase
from OOP.employee18 import Candidate


class CandidateTest(TestCase):

    def setUp(self):
        self.can = Candidate(firstname="Garry", lastname="Ermolenko", email="garffrfy@nure.ua", tech_stack=["Mysql", "Postgresql"], main_skill="fast coding", main_skill_grade="1st level")

    def test_name(self):
        self.assertEqual(self.can.name, "Garry Ermolenko")

    def test_generate_candidates(self):
        path = "/home/vadim/alevel/a-level-vadim/OOP/candidates.csv"
        expected_candidates = [
            Candidate("Ivan", "Chechov", "ichech@example.com", "Python|Django|Angular", "Python", "Senior"),
            Candidate("Max", "Payne", "mpayne@example.com", "PHP|Laravel|MySQL", "PHP", "Middle"),
            Candidate("Tom", "Hanks", "thanks@example.com", "Python|CSS", "Python", "Junior")
        ]
        self.assertEqual(Candidate.generate_candidates(path).__repr__(), expected_candidates.__str__())


          
          
