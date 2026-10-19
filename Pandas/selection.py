import pandas as pd

data = pd.read_csv("D:\Ai Ml learning\Pandas\All_Pokemon.csv", index_col = "Name")
# SELECTION BY COLUMN
# # print(data["Name"])
# # print(data["Height"])
# # print(data[["Height","Weight","Name"]].to_string())

# # SELECTION BY ROWS
# # there s index num labeled in the data but what u can do is to add / index_col = "" beside file name \
# print(data.loc["Pikachu"])
# print(data.loc["Charizard":"Blastoise",["Height","Weight"]])
# print(data.iloc[0:11,0:3]) # int based (how much size from 0 to 10 u want , how much col from 0 to 3 u want) 
search = str(input("enter a pokemon name : "))
try:
    print(data.loc[search])
except KeyError:
    print(f"{search} not found")
