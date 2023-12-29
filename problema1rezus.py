import pandas as pd
import matplotlib.pyplot as plt
import csv

class Employee:
    
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)
class Manager(Employee):
    mgr_count = 0
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"F26 {department}"
        Manager.mgr_count += 1

    def display_employee(self):
        X = 5 # 5%3=2
        if X % 3 == 0:
            print(f"Name: {self.name}")
        elif X % 3 == 1:
            print(f"Salary: {self.salary}")
        elif X % 3 == 2:
            print(f"Department: {self.department}")


Y = 12  
manager1 = Manager("Manager1", 60000, "IT")
manager2 = Manager("Manager2", 70000, "HR")
manager3 = Manager("Manager3", 80000, "Finance")
employee1 = Employee("John Doe", 50000)

manager1.display_employee()
manager2.display_employee()
manager3.display_employee()






print(f"Total number of manager(s) is {Manager.mgr_count}")
print(f"Total number of employee(s) is {Employee.empCount}")

