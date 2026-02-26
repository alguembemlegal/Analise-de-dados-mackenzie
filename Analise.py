#pip install pandas#

import pandas as pd

df = pd.read_csv('products-1000.csv', engine='xlrd', sheet_name=0)

print(df.head())