import pandas as pd
import matplotlib.pyplot as plt

x = [62, 80, 79, 72, 68, 66, 69, 68, 64, 77, 73, 70, 52, 89]

dados = pd.Series(x)

media = dados.mean()
mediana = dados.median()
moda = dados.mode()[0]

maximo = dados.max()
minimo = dados.min()
amplitude = maximo - minimo

variancia = dados.var()
desvio_padrao = dados.std()

q1 = dados.quantile(0.25)
q2 = dados.quantile(0.50)
q3 = dados.quantile(0.75)

amplitude_interquartil = q3 - q1

limite_inferior = q1 - 1.5 * amplitude_interquartil
limite_superior = q3 + 1.5 * amplitude_interquartil
outliers = dados[(dados < limite_inferior) | (dados > limite_superior)]


print(f"média: {media}, mediana: {mediana}, moda: {moda}, maximo: {maximo}, minimo: {minimo}, amplitude: {amplitude}")
print(f"variancia: {variancia}, desvio padrao: {desvio_padrao}")
print(f"Quartil 1: {q1}, Q2: {q2}, Q3: {q3}, amplitude interquartil: {amplitude_interquartil} outliers: {list(outliers)}")


plt.figure(figsize =(10,6))
plt.hist(dados, bins = 6)
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frequencia")

plt.show()

plt.subplot(1,2,2)
plt.boxplot(dados, vert=True)
plt.title("BoxPlot")

plt.tight_layout