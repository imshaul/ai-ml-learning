import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])



# aggregate functions
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.var(arr))
print(np.std(arr))

# filtering
print(arr[arr>5])
print(arr[arr<5])
print(arr[arr==5])
print(arr[arr==5])
print(arr[arr!=5])


# Random Numbers
num = np.random.randint(1,10)
print(num)
# Multiple random integers
multNum = np.random.randint(1,10,size=10)
print(multNum)
# Random Decimal
deci = np.random.rand(2)
print(deci)
# 2d array random
array = np.random.randint(1,10,size=(2,3))
print(array)
# SEED
seed = np.random.seed(9)
print(np.random.randint(1,10))