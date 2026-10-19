import numpy as np

marks = np.array([
    [1,42,63],
    [23,62,12],
    [64,95,32],
    [32,47,18]
])
print("info about data : ")
print(f"shape : {marks.shape} ; dimension : {marks.ndim} ; data type : {marks.dtype} ; data size : {marks.size}")
print("this is 2nd column : ")
print(marks[:,2])
print("2nd row data : ")
print(marks[2])
print("the mean of 2nd row data is : ")
print(np.mean(marks[:2]))
print(marks[marks[:,1]<80])