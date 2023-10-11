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


class Recruiter(Employee):

    def work(self):
        return "I come to the office and start to hiring."

class Developer(Employee):   

    def work(self):
        return "I come to the office and start to coding."


r = Recruiter("Nata", 20, "Master of recruting")
print(r.work())
print(r)

d = Developer("Vadim", 25, "Master of coding")
print(d.work())
print(d)

print(r > d)



