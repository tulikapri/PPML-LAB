#convert the series from string to numeric with error handelinh
import pandas as pd
s= pd.Series(['10','20','abc','30'])
s_numeric = pd.to_numeric(s, errors='coerce')
print(s_numeric)

