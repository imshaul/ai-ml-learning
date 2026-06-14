class Empolyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show_info(self):
        print(f"""Name:{self.name}
Salary:{self.salary}""")

class Manager(Empolyee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def show_Manager_info(self):
            print(f"""Name:{self.name}
Salary:{self.salary}
Department:{self.department}""")
 
m=Manager("Sahil",70500.55,"AI")
m.show_Manager_info()

















# Create:

# * `Employee`
# * `Manager`

# `Employee` should have:

# * name
# * salary
# * `show_info()`

# `Manager` should additionally have:

# * department

# Use inheritance properly.

# Concepts:

# * inheritance
# * `super()`
