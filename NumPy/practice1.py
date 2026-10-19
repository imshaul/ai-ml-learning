import numpy as np
class StudentAnalyzer:
    def __init__(self):
        self.students = np.array([
            ["Sahil",85,92,78],
            ["Rahul",81,95,43],
            ["Aman",74,91,97],
            ["Karan",84,52,86],
            ["Riya",95,49,60]
        ], dtype=object)
    def info(self):
        print(f"all students name : {self.students[:,0]}\n")
        print(f"complete student data : \n{self.students}\n")
        print(f"maths marks of all students : \n {self.students[:,1]} and the average marks is {np.mean(self.students[:,1])}")
        index = np.argmax(self.students[:,1])
        print(f"maths highest scorer is : {self.students[index,0]}")
        # avg_math_marks.mean = self.students[:,1]
        # print(avg_math_marks)
        marks_above = self.students[self.students[:,1]>80]  
        print(f"students who scored 80+ in maths exam : \n{marks_above}")
        marks_below = self.students[self.students[:,3]<50]
        print(f"students who scored 50- in english exam : \n{marks_below[:,0]}")
    def grace(self):
        self.students[:,2] += 8
        print(f"new science marks (grace marks included)\n{self.students}")
    def some_info(self):
        print("some info related to dataset : \n")
        print(self.students.shape)
        print(self.students.size)
        print(self.students.dtype)
    def searching(self):
     try:
        user = str(input("enter the name u wanna find : "))
        for std in self.students:
            if user.lower() == std[0].lower():
                print(f"{std} found!!")
                break
            else :
                print("not found")
                break
     except:
            print("invalid input")
            
        
s = StudentAnalyzer()
s.info()
s.grace()
s.some_info()
s.searching()