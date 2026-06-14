import numpy as np

marks = np.array([
    [85,90,78],
    [92,93,74],
    [62,75,79],
    [86,65,75],
    [94,94,85]
])

# Array infomation
print(f"Number of dimensions: {np.ndim(marks)}")
print(f"Shape: {np.shape(marks)}")
print(f"Total elements: {np.size(marks)}")

# Slicing

print(f"First Student marks are : {marks[0]}")
print(f"Last Student marks are : {marks[4]}")
print(f"Whole class Maths marks: {marks[:,0]}")

# Filtering
print("Scores above 90:")
print(marks[marks>90])

# Boardcasting

bonus = np.array([5,5,5])
new_marks= marks+bonus
print(f"New Marks :")
print(new_marks)

# Arthmetic

percentage = (marks/100)*100
print(f"Percentage:")
print(percentage)