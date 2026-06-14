class Student:
    class_year=0
    num_students=0
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        Student.num_students+=1

student1=Student("Sahil",18,4567)
student2=Student("abcd",19,4568)
print(student1.name)
print(student2.name)
print(Student.num_students)
