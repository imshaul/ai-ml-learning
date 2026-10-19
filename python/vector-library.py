class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector {self.x,self.y}"
    def __len__(self):
        return f"{self.x ,self.y}"
    def __eq__(self,other):
        return self.x == other.x
    def __add__(self,other):
        return self.x + other.x
    def __gt__(self,other):
        return self.x>other.x
    def __call__(self):
        return "Hello how are u"

v1 = Vector(4,7)
v2 = Vector(8,3)
print(v1)
print(v1+v2)
print(v1==v2)
print(v1>v2)
v1
