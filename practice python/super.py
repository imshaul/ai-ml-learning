class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("Employee const called")

    def show_info(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
        print("Manager const is called")

    def show_depo(self):
        print("Department:",self.department)

m=Manager("Sahil",40000,"Ai block")
m.show_info()