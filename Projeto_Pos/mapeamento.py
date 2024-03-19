import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from datetime import datetime

# Verificar se o arquivo de resumo já existe
arquivo_resumo = "resumo.xlsx"
is_excel = False
try:
    pd.read_excel(arquivo_resumo)
    is_excel = True
except Exception:
    pass

if not is_excel:
    # Criar um DataFrame vazio com as colunas desejadas e salvar como uma nova planilha
    pd.DataFrame(columns=["cliente", "cnpj", "data do contato", "responsavel", "faturamento", "detalhe do contato"]).to_excel(
        arquivo_resumo, index=False
    )

# Carregar a planilha de faturamento
planilha_faturamento = pd.read_excel(arquivo_resumo)

# Verificar se há dados suficientes para fazer previsões
if len(planilha_faturamento) < 2:
    print("Não há dados suficientes para fazer previsões futuras.")
else:
    # Converter a coluna "data do contato" para o formato de data
    planilha_faturamento["data do contato"] = pd.to_datetime(planilha_faturamento["data do contato"], dayfirst=True)

    # Obter a data atual
    data_atual = pd.to_datetime(datetime.now().date())

    # Calcular as estatísticas com base nos dados atuais e imprimir
    print("Estatísticas com base nos dados atuais:")
    print(planilha_faturamento[planilha_faturamento["data do contato"] <= data_atual].describe())

    # Criar uma lista para armazenar as informações de cada cliente
    clientes = []

    # Iterar sobre cada cliente
    for cliente in planilha_faturamento["cliente"].unique():
        # Filtrar os dados do cliente atual
        dados_cliente = planilha_faturamento[planilha_faturamento["cliente"] == cliente]

        # Verificar se o cliente está apto a crédito ou consórcio
        ultimo_faturamento = dados_cliente["faturamento"].max()
        oportunidade = ""
        if ultimo_faturamento <= 100:
            oportunidade = "Crédito"
        elif ultimo_faturamento > 100:
            oportunidade = "Consórcio"

        # Adicionar as informações do cliente à lista
        clientes.append({"cliente": cliente, "cnpj": dados_cliente["cnpj"].iloc[0], "faturamento_atual": ultimo_faturamento, "oportunidade_atual": oportunidade})

    # Previsões futuras para cada cliente
    for cliente in clientes:
        # Filtrar os dados do cliente atual
        dados_cliente = planilha_faturamento[planilha_faturamento["cliente"] == cliente["cliente"]]

        # Preparar os dados para o modelo de regressão linear
        meses = np.arange(len(dados_cliente))
        faturamento = dados_cliente["faturamento"].values

        # Normalizar os dados
        meses_normalizados = (meses - meses.min()) / (meses.max() - meses.min())
        faturamento_normalizado = (faturamento - faturamento.min()) / (faturamento.max() - faturamento.min())

        # Criar e treinar o modelo de regressão linear usando TensorFlow
        modelo = tf.keras.Sequential([
            tf.keras.layers.Dense(units=1, input_shape=[1])
        ])
        modelo.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
        modelo.fit(meses_normalizados, faturamento_normalizado, epochs=1000, verbose=0)

        # Prever o próximo mês com base nos dados anteriores do cliente
        mes_futuro = np.array([[meses.max() + 1]])
        mes_futuro_normalizado = (mes_futuro - meses.min()) / (meses.max() - meses.min())
        faturamento_previsto_normalizado = modelo.predict(mes_futuro_normalizado)
        faturamento_previsto = faturamento_previsto_normalizado * (faturamento.max() - faturamento.min()) + faturamento.min()

        # Armazenar a oportunidade para o próximo mês
        previsao_prox_mes = int(np.squeeze(faturamento_previsto))
        oportunidade_prox_mes = ""
        if previsao_prox_mes <= 100:
            oportunidade_prox_mes = "Crédito"
        elif previsao_prox_mes > 100:
            oportunidade_prox_mes = "Consórcio"

        # Atualizar as informações do cliente na lista
        cliente["previsao_prox_mes"] = previsao_prox_mes
        cliente["oportunidade_prox_mes"] = oportunidade_prox_mes

        # Adicionar o faturamento na lista do cliente
        cliente["faturamento"] = faturamento.tolist()

        # Limpar a sessão do TensorFlow para evitar confusão entre iterações do loop
        tf.keras.backend.clear_session()

    # Imprimir as oportunidades de oferta para cada cliente
    for cliente in clientes:
        print(f"Cliente: {cliente['cliente']}")
        print(f"CNPJ: {cliente['cnpj']}")
        print(f"Faturamento atual: {cliente['faturamento_atual']}, oferecer: {cliente['oportunidade_atual']}")
        print(f"Faturamento: {cliente['faturamento']}")
        print(f"Previsão do próximo mês: {cliente['previsao_prox_mes']}, oportunidade de oferecer: {cliente['oportunidade_prox_mes']}")
        print()
        
        # Exibir a explicação da previsão
print(f"Explicação da previsão para o próximo mês do cliente {cliente['cliente']}:")
print(f"O valor previsto para o próximo mês é {previsao_prox_mes}.")
print("O cálculo da previsão foi realizado da seguinte forma:")
print(f"1. Normalizamos o valor do último mês ({faturamento[-1]}) para o intervalo entre 0 e 1.")
print(f"2. Utilizamos o modelo treinado para prever a próxima entrada normalizada, obtendo o valor {faturamento_previsto_normalizado}.")
print(f"3. Desnormalizamos o valor previsto para o intervalo original de faturamento ({faturamento.min()} a {faturamento.max()}), resultando em {faturamento_previsto}.")
print()