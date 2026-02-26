#pip install pandas#

import pandas as pd

df = pd.read_csv('products-1000.csv')

print("Mostra o nome das colunas do dataframe =", df.columns)
print("Mostra o conteúdo das colunas Price = \n", df['Price'])

#media_preco = df['Price'].mean() print("media preço = ", media_preco) para usar a biblioteca panda

def media(v):
    n = len(v)
    soma = 0
    for i in range(n):
        soma = soma + v[i]
    soma = soma / n
    return soma

resultado = media(df['Price'])
print("Média dos preços", resultado)
