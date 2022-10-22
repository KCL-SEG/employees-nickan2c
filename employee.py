"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, salary=0, hourlyPay=0, hours=0, commissionPerContract=0, bonusComission=0, nContracts=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourlyPay = hourlyPay
        self.commissionPerContract = commissionPerContract
        self.bonusComission = bonusComission
        self.nContracts = nContracts

    def get_pay(self):
        return self.salary + (self.hours * self.hourlyPay) + (
                    self.nContracts * self.commissionPerContract) + self.bonusComission

    def __str__(self):
        # Charlie works on a contract of 100 hours at 25/hour.\s+Their total pay is 2500.
        toReturn = self.name + " works on a "
        if self.salary > 0:
            toReturn += "monthly salary of " + str(self.salary)
        else:
            toReturn += "contract of " + str(self.hours) + " hours at " + str(self.hourlyPay) + "/hour"

        if self.nContracts > 0:
            toReturn += " and receives a commission for " + str(self.nContracts) + " contract(s) at " + str(
                self.commissionPerContract) + "/contract"
        elif self.bonusComission > 0:
            toReturn += " and receives a bonus commission of " + str(self.bonusComission)

        toReturn += ". Their total pay is " + str(self.get_pay()) + "."
        return toReturn


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)
print(billie)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100, 0, 0, 0)
print(charlie)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 200, 0, 4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 220, 0, 3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 1500, 0)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 0, 600, 0)
