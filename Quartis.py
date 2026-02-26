import pandas as pd

df = pd.read_csv('products-1000.csv')

#df['Price'] = pd.to_numeric(df['Price'], errors='coerce') quartis usando a biblioteca pandas

#quartis = df['Price'].quantile([0.25, 0.5, 0.75])

#print(quartis)

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

def quartis(v):
    n = len(v)
    vo = sorted(v)
    medq1, posq1 = mediana_e_posição(vo)
    q2 = medq1
    medq2, posq2 = mediana_e_posição(vo[1:(posq1 - 1)])
    q1 = medq2
    medq3, posq3 = mediana_e_posição(vo[(posq1 + 1): n])
    q3 = medq3
    return q1,q2,q3

q1,q2,q3 = quartis(df['Price'])

print("Q1 =", q1)
print("Q2 =", q2)
print("Q3 =", q3)