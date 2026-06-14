class BankAccount:
    bank_name="SBI"
    def __init__(self,name,acc_num,credited,debited):
        self.name=name
        self.acc_num=acc_num
        self.credited=credited
        self.debited=debited

    def show_balance(self):
        remaining=self.credited-self.debited
        print(f"""Name:{self.name}
Acc Number:{self.acc_num}"""
        )
        if remaining<0:
            print("insufficient balance")
        else:
            print("OKAYYYYY")
            print(f"Balance:{remaining}")

print(BankAccount.bank_name)
user1=BankAccount("Sahil",5848548921,60000,70000)
user1.show_balance()




