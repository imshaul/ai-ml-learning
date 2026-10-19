import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Headphones", "Laptop", "Keyboard", "Phone", "Mouse"],
    "Category": ["Electronics", "electronics", "Audio", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 30000, None, 60000, 2500, 30000, 800],
    "Quantity": [2, 5, 10, 2, None, 5, 15],
    "City": ["Chandigarh", "Delhi", "Chandigarh", "Chandigarh", None, "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

print(df)