class Employee:
    def __init__(self, name, salary_day, job_title):
        self.employee_name = name
        self.salary_for_day = salary_day
        self.job_title = job_title
    

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


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."


class Developer(Employee):
    def __init__(self, name, salary_day, job_title, tech_stack):
        self.stack = tech_stack
        super().__init__(name, salary_day, job_title)
        
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
        return Developer(self.employee_name + " " + other.employee_name, self.combined_bigger_salary(other), "Developer", list(set(self.stack + other.stack)))
    

r = Recruiter("Nata", 20, "Master of recruting")
print(r.work())
print(r)
print(r.check_salary(14))

d_1 = Developer("Vadim", 25, "Master of coding", ["Python", "Django", "Mysql", "Postgresql", "HTML", "CSS", "JS"])
print(d_1.work())
print(d_1)
print(d_1.check_salary(28))

print(r > d_1)

d_2 = Developer("John", 29, "Master of testing", ["QA", "Python", "Mysql", "Postgresql", "HTML", "CSS"])

print(d_1 > d_2)

d_3 = d_1 + d_2
print(d_3)
