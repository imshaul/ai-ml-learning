class Father:
    car = "Mustang"
    house = "villa"
    net_Worth = 500000
    
    def show_details(self):
        print(f"""Car : {self.car}
House : {self.house}
net_Worth : {self.net_Worth}""")

class Child(Father):
    worth = 600000
    def showdetails(self):
        print(f"""Car : {self.car}
House : {self.house}
net_Worth : {self.net_Worth + self.worth}""")

c = Child()
c.showdetails()
