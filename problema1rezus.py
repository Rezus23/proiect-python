import pandas as pd
import matplotlib.pyplot as plt
import csv

class Employee:
    emp_count = 0

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.emp_count += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary, "F26_" + department)
        Manager.mgr_count += 1

    def display_employee(self):
        X=5
        remainder = X % 3 #5%3=2
        if remainder == 0:
            print(f"Name: {self.name}")
        elif remainder == 1:
            print(f"Salary: {self.salary}")
        elif remainder == 2:
            print(f"Department: {self.department}")



Y = 12

manager1 = Manager("Rezus Catalin",2304050,"BOSS")
manager2 = Manager("Fertiliu Claudiu",2345,"HR")
manager3 = Manager("CanUT fermilian",20055554,"IT")

manager1.display_employee()
manager2.display_employee()
manager3.display_employee()



print(f"Total number of manager(s) is {Manager.mgr_count}")
print(f"Total number of employee(s) is {Employee.emp_count}")

