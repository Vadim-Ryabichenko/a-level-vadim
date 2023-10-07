import csv
from datetime import datetime
import traceback

now = datetime.now()

class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, salary_day, job_title, email):
        self.employee_name = name
        self.salary_for_day = salary_day
        self.job_title = job_title
        self.email = email
        self.save_email()

    def __str__(self):
        return f"{self.job_title} : {self.employee_name}"

    def work(self):
        return "I come to the office."
    
    def __gt__(self, other):
        return self.salary_for_day > other.salary_for_day
        
    def check_salary(self, days):
        first = days // 6
        second = days // 7
        working_days = days - first - second
        return f"Salary for {days} days = {self.salary_for_day * working_days} dollars"
    
    def save_email(self):
        self.validate()
        with open("/home/vadim/alevel/a-level-vadim/OOP/emails.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([self.email])
    
    def validate(self):
        with open("/home/vadim/alevel/a-level-vadim/OOP/emails.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if self.email in row:
                    raise EmailAlreadyExistsException(f"email {self.email} already exist in emails.csv")            


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."


class Developer(Employee):
    def __init__(self, name, salary_day, job_title, tech_stack, email):
        self.stack = tech_stack
        super().__init__(name, salary_day, job_title, email)
        
    def work(self):
        return "I come to the office and start to coding."

    def __gt__(self, other):
        return len(self.stack) > len(other.stack)
        
    def combined_bigger_salary(self, other):
        if self.salary_for_day > other.salary_for_day:
            return self.salary_for_day
        else: 
            return other.salary_for_day 
            
    def __add__(self, other):
        return Developer(self.employee_name + " " + other.employee_name, self.combined_bigger_salary(other), "Developer", list(set(self.stack + other.stack)), self.email + " or " + other.email)


class Candidate:
    def __init__(self, firstname, lastname, email, tech_stack, main_skill, main_skill_grade):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email} {self.tech_stack} {self.main_skill} {self.main_skill_grade}"
    
    def __repr__(self):
        return f"{self.firstname} {self.lastname} {self.email} {self.tech_stack} {self.main_skill} {self.main_skill_grade}"

    @property
    def name(self):
        return f'{self.firstname} {self.lastname}'
    
    @classmethod
    def generate_candidates(cls, path):
        candidates_l = []
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                candidates_l.append(
                    Candidate(
                        (row["Full Name"]).split()[0], 
                        (row["Full Name"]).split()[1], 
                        row["Email"], 
                        row["Technologies"], 
                        row["Main Skill"], 
                        row["Main Skill Grade"]
                        )
                        )
        return candidates_l

try:
    r = Recruiter(
        "Nata", 
        20, 
        "Master of recruting", 
        "nata@gmail.com"
        )
    print(r.work())
    print(r)
    print(r.check_salary(14))

    d_1 = Developer(
        "Vadim", 
        25, 
        "Master of coding", 
        ["Python", "Django", "Mysql", "Postgresql", "HTML", "CSS", "JS"], 
        "vadim@gmail.ua"
        )
    print(d_1.work())
    print(d_1)
    print(d_1.check_salary(28))

    print(r > d_1)

    d_2 = Developer(
        "John", 
        29, 
        "Master of testing", 
        ["QA", "Python", "Mysql", "Postgresql", "HTML", "CSS"], 
        "john@gmail.ua"
        )

    print(d_1 > d_2)

    d_3 = d_1 + d_2
    print(d_3)

    r_2 = Recruiter("Katya", 35, "Master of recruting", "katya@gmail.com")
except EmailAlreadyExistsException:
    with open("/home/vadim/alevel/a-level-vadim/OOP/logs.txt", "a") as file:
        file.write(f"%{now.date()}% %{now.time()}% | %{traceback.format_exc()}%")


c = Candidate("Lola", "Grinchenko", "fast coding", "1st level", "lola@gmail.com", ["Mysql", "Postgresql"])
print(c.name)

print(Candidate.generate_candidates("/home/vadim/alevel/a-level-vadim/OOP/candidates.csv"))
print(Candidate.generate_candidates("/home/vadim/alevel/a-level-vadim/OOP/candidates.csv")[0])
    