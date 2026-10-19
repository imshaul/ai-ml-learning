import pandas as pd

data = pd.read_csv("D:\Ai Ml learning\Pandas\All_Pokemon.csv")
# DATA INFORMATION TO UNDERSTAND DATA
# print(data.head())
# print(data.tail())
# print(data.shape)
# print(data.info)
print(data.describe())

# DROP IRRELEVENT COLUMNS
# data = data.drop(columns = ["Legendary","Number"])
# print(data.columns)

# HANDLE MISSING DATA
# data = data.dropna(subset = ["Type2"])
data = data.fillna({"Type 2":"None"})
data["Type 1"] = data["Type 1"].replace({"Grass":"GRASS",
                                        "Fire":"FIRE"})
# STANDARIZE
# data["Name"] = data["Name"].str.lower()
# FIX DATA TYPES
data["Height"] = data["Height"].astype(int)

# REMOVE DUPLICATE
data = data.drop_duplicates()
# print(data)

#OUTLINER DETECTION
data.rename(columns = {"Height":"Hgt"},inplace=True)
print(data)