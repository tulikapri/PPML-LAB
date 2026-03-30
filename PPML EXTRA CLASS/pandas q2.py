import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "City": ["Delhi", "Mumbai", "Kolkata"]
}

df = pd.DataFrame(data)

print(df)