import pandas as pd

data = {
    "Name":["Sahil","Divyanshu","Aryan","Priya"],
    "Age":["18","18","17","19"]
}
df=pd.DataFrame(data)
df[df["Age"<18]]
print(df)