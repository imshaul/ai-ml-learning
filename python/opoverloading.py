# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.players = ["A","B","C"]

#     def __str__(self):
#         return f"Vector {self.x} + {self.y}"
# class Team:
#     def __init__(self):
#         self.players = ["A","B","C"]

#     def __len__(self):
#         return len(self.players)

# class Library:
#     def __init__(self):
#         self.books = ["Harry potter", "Magic morals", "DeathNote"]
#     def __getitem__(self,index):
#         return self.books[index]
#     def __iter__(self):
#         return iter(self.books)

class Math:
    # def __init__(self,x):
    #     self.x = x
    # def __add__(self,other):
    #     return f"Addition : {self.x + other.x}"
    def __call__(self):
        print(self)

# v = Vector(5,6)
# print(v)
# t = Team()
# print(len(t))
# b = Library()
# print(b[0])
# print(b[1])
# for book in b:
#     print(book)
# m = Math(4)
# m2 = Math(1)
# print(m + m2)
m = Math()
m()