import pandas as pd
marks = pd.Series(
    [1,2,4],
    index = ["Sahil","Karan","Vanshika"]
    )
print(marks)
student_data = {
    "Name":["Sahil","Karan","Rohit"],
    "Age":[18,19,19]
} 
print(pd.DataFrame(student_data))
