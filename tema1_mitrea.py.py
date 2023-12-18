

class Employee:
    
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        
        print("Total number of employees is ",Employee.empCount)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

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
        X = 6
        if X % 3 == 0:
            print(f"Name: {self.name}")
        elif X % 3 == 1:
            print(f"Salary: {self.salary}")
        elif X % 3 == 2:
            print(f"Department: {self.department}")
Y = 11  
manager1 = Manager("Mitrea Tudor", 100000, "IT")
manager2 = Manager("Rezus Catalin", 110000, "IT")
manager3 = Manager("Silviu Ionut", 80000, "DevOps")

employee1= Employee("Cocos Lavrente",100)


manager1.display_employee()
manager2.display_employee()
manager3.display_employee()





print(f"Total number of manager(s) is {Manager.mgr_count}")
print(f"Total number of employee(s) is {Employee.empCount}")

