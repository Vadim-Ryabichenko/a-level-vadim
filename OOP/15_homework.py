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
        if self.salary_for_day > other.salary_for_day:
            return f"Salary {self.employee_name} bigger than {other.employee_name}"
        else:
            return f"Salary {self.employee_name} smaller than {other.employee_name}"

class Recruiter(Employee):
    
    def work_recruiter(self):
        return super().work()[:len(super().work()) - 1] + " and start to coding."

class Developer(Employee):   
    
    def work_developer(self):
        return super().work()[:len(super().work()) - 1] + " and start to hiring."
    

r = Recruiter("Nata", 20, "Master of recruting")
print(r.work())
print(r.work_recruiter())
print(r)

d = Developer("Vadim", 25, "Master of coding")
print(d.work())
print(d.work_developer())
print(d)

print(r > d)


