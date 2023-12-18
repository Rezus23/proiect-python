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
        self.department = f"F26grup_{department}"
        Manager.mgr_count += 1

    def display_employee(self):
        x = Manager.mgr_count % 3
        if x == 0:
            print(f"Name: {self.name}")
        elif x == 1:
            print(f"Salary: {self.salary}")
        elif x == 2:
            print(f"Department: {self.department}")


Y = 12  
managers = [Manager(f"Manager{i}", i * 1000, f"Department{i % 3}") for i in range(Y // 3)]



for manager in managers:
    manager.display_employee()


for i in range(Employee.empCount):
    Employee.display_employee(managers[i % (Y // 3)])


print(f"Total number of manager(s) is {Manager.mgr_count}")

df = pd.read_csv('data.csv')
df.plot(title='Toate valorile')
plt.show()
X = 5 
df.head(X).plot(title=f'primele {X} valori')
plt.show()
df.tail(Y)[['Durata', 'Puls']].plot(title=f'ultimele {Y} valori pentru  Durata si Puls')
plt.show()