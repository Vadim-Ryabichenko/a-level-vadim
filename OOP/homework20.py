import csv
from datetime import datetime
import traceback


now = datetime.now()


class EmailAlreadyExistsException(Exception):
    pass


class Writer:
    def write(self, s):
        self.s = s
        with open("writer.txt", "a") as file:
            file.write(s)

                
class Logger:

    my_writer = Writer()
    
    def write(self, exception):
        number = self.get_error_number()
        error_class = type(exception).__name__
        error_message = str(exception)
        log_string = f"{number}\t{now.date()} {now.time()}\t{error_class}\t{error_message}\n"
        self.my_writer.write(log_string)

    def get_error_number(self):
        with open("writer.txt") as file:
            lines = file.readlines()
            number = len(lines) + 1
        return number

def logger(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as exception:
            logger_instance = Logger()
            logger_instance.write(exception)
    return wrapper


class Employee:
    def __init__(self, name, salary_day, job_title, email):
        self.employee_name = name
        self.salary_for_day = salary_day
        self.job_title = job_title
        self.save_email(email)

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
    
    def save_email(self, email):
        try:
            self.validate(email)
            self.email = email
            with open("emails.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([self.email])
        except EmailAlreadyExistsException:
            with open("logs.txt", "a") as file:
                file.write(f"%{now.date()}% %{now.time()}% | %{traceback.format_exc()}%")
            raise
    
    @logger
    def validate(self, email):
        with open("emails.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if email in row:
                    raise EmailAlreadyExistsException(f"email {email} already exist in emails.csv")            


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
        return Developer(self.employee_name + " " + other.employee_name, 
                         self.combined_bigger_salary(other), 
                         "Developer", 
                         list(set(self.stack + other.stack)), 
                         self.email + " " +  other.email)


class Candidate:
    def __init__(self, firstname, lastname, email, tech_stack, main_skill, main_skill_grade):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email}" # як допоміжна функція для тесту

    def __repr__(self):
        return self.__str__()  # як допоміжна функція для тесту

    @property
    def name(self):
        return f'{self.firstname} {self.lastname}'
    
    @classmethod
    @logger
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
                        row["Main Skill Grade"],
                        row["hobby"]
                        )
                        )
        return candidates_l


if __name__ == "__main__":

    c = Candidate("Lola", "Grinchenko", "fast coding", "1st level", "lola@gmail.com", ["Mysql", "Postgresql"])
    print(c.name)

    print(Candidate.generate_candidates("candidates.csv"))
 
