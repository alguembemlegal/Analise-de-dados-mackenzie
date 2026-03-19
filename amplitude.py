import pandas as pd

df = pd.read_csv('products-1000.csv')

df['Price'] = pd.to_numeric(df['Price'], errors='coerce') #calcular amplitude via pandas

#amplitude = df['Price'].max() - df['Price'].min()

#print("Amplitude =", amplitude)

