# def my_generator():
#     for i in range(700*64):
#         yield i

# gen = my_generator()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# for j in gen:
#     print(j)

def number():
    yield 10
    yield 20
    yield 30
gen = number()
print(next(gen))
print(next(gen))
print(next(gen))