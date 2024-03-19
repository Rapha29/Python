import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dias_anteriores = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Números de dias anteriores
valores_do_dolar = np.array([5.0, 5.2, 5.1, 5.4, 5.5])  # Valores do dólar nos dias anteriores

# Criar e treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(dias_anteriores, valores_do_dolar)

# Prever o valor do dólar no próximo dia (dia 6)
proximo_dia = np.array([6]).reshape(-1, 1)
previsao = modelo.predict(proximo_dia)

print(f"A previsão do valor do dólar no próximo dia é: {previsao[0]:.2f}")
