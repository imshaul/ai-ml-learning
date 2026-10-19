class Person:
    def __init__(self):
        self.__name = "Sahil"

s = Person() 
# cant run
# print(s.__name) 
# can run
print(s._Person__name) 
# this will show all methods and everything used
print(s.__dir__())
