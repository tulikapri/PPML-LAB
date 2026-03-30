import pandas as pd
s=pd.Series(['apple', 'banana', 'apple', 'orange'])
#convert to categoral
cat_s=s.astype('category')
print(cat_s.cat.codes)