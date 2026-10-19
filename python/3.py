class Manager:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def role(self):
        print("your role is manager")

class Employee(Manager):
    def __init__(self):
        super().__init__()
    def role(self):
          print("your role is machine learning engineer")

m = Manager("Sahil",850)
e = Employee("Pihu",254)
m.role()
e.role()