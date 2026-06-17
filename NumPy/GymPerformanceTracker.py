import numpy as np
class GymTracker:
    def __init__(self,name,data):
        self.name=name
        self.data=np.array(data)
     

    def show_data(self):
        print(self.name)
        print(self.data)

    def dataset_info(self):
        print(np.ndim(self.data))
        print(np.size(self.data))
        print(np.shape(self.data))
    
    def member_status(self):
        print(f"First member status:{self.data[0]}")
        print(f"Second member status:{self.data[1]}")
        print(f"Third member status:{self.data[2]}")

    def bonus(self):
        add=np.array([4,6,8])
        new = add + self.data
        print(new)

    def elite_members(self):
        self.data[self.data >= 70]
        print("💪💯")

gym_data = [
    [40, 60, 10],
    [50, 80, 12],
    [30, 55, 8],
    [70, 90, 15],
    [45, 65, 11]
]

member1=GymTracker("Sahil",gym_data)
member1.show_data()
member1.dataset_info()
member1.member_status()
member1.bonus()
member1.elite_members()