import pandas as pd

# Importing Data

imp = pd.read_csv("Pandas/data_dictionary.csv")
imp.head()
imp.tail()
imp.info()
print("--------------------------------------------------------------------------------")
# Print full data
print(imp)
print(imp["Column"])

print("--------------------------------------------------------------------------------")
Selects row using loc

print(imp.loc[0])

print("--------------------------------------------------------------------------------")
# Selects specific cell using loc
print(imp.loc[0,"Description"])
# Selects row by position
print(imp.iloc[4])
# Selects specific cell using iloc
print(imp.iloc[3,1])
print("--------------------------------------------------------------------------------")