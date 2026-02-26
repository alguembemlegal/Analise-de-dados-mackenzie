import pandas as pd

df = pd.read_csv('products-1000.csv')

#df['Price'] = pd.to_numeric(df['Price'], errors='coerce') para usar a biblioteca pandas

#mediana = df['Price'].median()

#print("Mediana dos preços =", mediana)

def mediana_e_posição(v):
    n = len(v)
    vo = sorted(v)
    if n % 2 == 0:
        ni = int(n/2)
        mediana = (vo[ni-1] + vo[ni]) /2
    else:
        ni = int(n/2)
        mediana = vo[ni]
    return mediana, ni

resultado = mediana_e_posição(df['Price'])
print("mediana dos preços", resultado)