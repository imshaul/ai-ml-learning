import pandas as pd

# Series
s = pd.Series(
    [34,56,78],
    index=["Sahil","Divyanshu","Aryan"]
)
print(s["Sahil"])
print(s["Divyanshu"])
print("---------------")
print(s)
print("---------------")
# Series from Dictionary
data = {
    "Sahil":18,
    "Aryan":17
 }
show_info = pd.Series(data)
print(show_info)
print("--------------")

# DataFrames

student_data = {
    "Name":["Sahil","Aryan","Divyanshu"],
    "Age":[18,17,18]
}
df = pd.DataFrame(student_data)
print(df)
print("--------------")
