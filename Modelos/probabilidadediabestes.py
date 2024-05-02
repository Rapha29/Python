import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Fazendo a requisição para a API para obter os dados históricos do dólar
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()
rates = data['rates']

# Extrair as datas e os valores de fechamento do dólar
dates = []
values = []
for date, value in rates.items():
    dates.append(date)
    values.append(value)

# Converter as datas em números sequenciais
dates = np.arange(len(dates))

# Converter os valores de fechamento em formato float
values = np.array(values, dtype=float)

# Obter o valor do dólar hoje
today_value = values[-1]

# Dividir os dados em treinamento e teste
split_index = int(0.8 * len(dates))
train_dates, test_dates = dates[:split_index], dates[split_index:]
train_values, test_values = values[:split_index], values[split_index:]

# Treinamento do modelo de regressão linear
model = LinearRegression()
model.fit(train_dates.reshape(-1, 1), train_values)

# Previsões do modelo em um intervalo futuro
future_dates = np.arange(len(dates), len(dates) + 10).reshape(-1, 1)
future_predictions = model.predict(future_dates)

# Plotar os dados históricos e as previsões do modelo
plt.figure(figsize=(10, 6))
plt.plot(dates, values, label='Dados Históricos')
plt.plot(future_dates, future_predictions, color='red', linewidth=2, label='Previsão Futura')
plt.axhline(y=today_value, color='orange', linestyle='--', label='Valor Atual')
plt.xlabel('Datas')
plt.ylabel('Valor do Dólar')
plt.title('Previsão Futura do Valor do Dólar')
plt.legend()
plt.show()