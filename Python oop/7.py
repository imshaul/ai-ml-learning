class Teacher:

    def __init__(self, name, subject):

        self.name = name
        self.subject = subject

    def show_teacher(self):

        print(f"Teacher: {self.name} | Subject: {self.subject}")


class Department:

    def __init__(self, department_name):

        self.department_name = department_name

        self.teachers = []

    def add_teacher(self, teacher):

        self.teachers.append(teacher)

    def show_teachers(self):

        print(f"\nDepartment: {self.department_name}\n")

        for teacher in self.teachers:

            teacher.show_teacher()


teacher1 = Teacher("Sahil", "Python")

teacher2 = Teacher("Chahek", "AI")

teacher3 = Teacher("Raj", "Math")


department = Department("Computer Science")


department.add_teacher(teacher1)

department.add_teacher(teacher2)

department.add_teacher(teacher3)


department.show_teachers()