import csv

class Telephone:

    number = '0000000000'
    _counter = 0

    def set_number(self, new_number):
        self.number = new_number
    
    def get_accepted_calls(self, amount = 0):
        amount = self._counter
        return amount

    def accept_call(self):
        self._counter += 1

first_telephone = Telephone()
second_telephone = Telephone()
third_telephone = Telephone()

first_telephone.set_number("0992105443")
second_telephone.set_number("0951978433")
third_telephone.set_number("0683568799")

first_telephone.accept_call()
first_telephone.accept_call()

second_telephone.accept_call()
second_telephone.accept_call()
second_telephone.accept_call()
second_telephone.accept_call()

third_telephone.accept_call()
third_telephone.accept_call()
third_telephone.accept_call()
third_telephone.accept_call()
third_telephone.accept_call()
third_telephone.accept_call()

first_telephone.accept_call()

def counter_func_sum(telephones):
    result = 0
    for telephone in telephones:
       result += telephone.get_accepted_calls()
    return result

with open("/home/vadim/a_level_vadim/OOP/telephones.csv", "w") as file:
    push = counter_func_sum([first_telephone, second_telephone, third_telephone])
    writer = csv.writer(file)
    writer.writerow(['Count calls =', push])  
