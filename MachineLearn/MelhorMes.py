import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import datetime

dados = pd.read_excel('dados_clientes.xlsx')  

X = dados[['Mês']].values.reshape(-1, 1)
Y = dados['Saldo Bancário'].values

# Obter o mês atual
mes_atual = datetime.now().month

# Encontrar o saldo bancário correspondente ao mês atual
saldo_atual = dados[dados['Mês'] == mes_atual]['Saldo Bancário'].values[0]

mes_emprestimo = None
mes_consorcio = None

# Calcular a média dos saldos de cada mês
media_saldos_por_mes = dados.groupby('Mês')['Saldo Bancário'].mean()

# Determinar o mês mais propenso para contratar um empréstimo (menor saldo médio)
mes_emprestimo = media_saldos_por_mes.idxmin()

# Determinar o mês mais propenso para contratar um consórcio (maior saldo médio)
mes_consorcio = media_saldos_por_mes.idxmax()

# Calcular a projeção do saldo bancário para o próximo mês com base no modelo de regressão linear
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size=0.2, random_state=42)
modelo = LinearRegression()
modelo.fit(X_treino, Y_treino)

meses_futuros = np.array([[mes_atual + 1]])
saldo_previsto_proximo_mes = modelo.predict(meses_futuros)[0]

# Mostrar a data de hoje e os resultados
data_hoje = datetime.now().strftime("%d-%m-%Y")
print("Data de hoje:", data_hoje)
print("\nO Saldo atual da conta este mês (", mes_atual, ") é de: ", saldo_atual)
print("\nMês mais propenso para contratar um empréstimo:", mes_emprestimo)
print("\nMês mais propenso para contratar um consórcio:", mes_consorcio)
print("\nProjeção do saldo bancário para o próximo mês com base no mês atual:", saldo_previsto_proximo_mes)
