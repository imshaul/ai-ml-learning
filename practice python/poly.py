from abc import ABC,abstractclassmethod
class Payment(ABC):
    def __init__(self,user):
        self.user=user
        print(f"{self.name} Credited")