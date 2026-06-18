class Student:
    college_name="Harvard"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show_details(self):
        print(f"The Student name is {self.name} and the marks are {self.marks}")
        
student1=Student("Sahil",97)
student2=Student("abcd",99)
student1.show_details()
student2.show_details()
print(Student.college_name) 
#