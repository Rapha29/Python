from dash import Dash, html, dcc, Input, Output
import requests
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression

app = Dash(__name__)

# Função para prever o valor do dólar com base nos dados históricos
def prever_valor_dolar(dias_anteriores, valores_do_dolar, proximo_dia):
    modelo = LinearRegression()
    modelo.fit(dias_anteriores, valores_do_dolar)
    previsao = modelo.predict(np.array([proximo_dia]).reshape(-1, 1))
    return previsao[0]

url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/30'
response = requests.get(url)
data = response.json()

dates = []
dollars = []

for item in data:
    try:
        date = pd.to_datetime(int(item['timestamp']), unit='s')
        dollar_value = float(item['bid'])

        if not pd.isnull(date):
            dates.append(date)
            dollars.append(dollar_value)
        else:
            print(f"Data inválida: {item['timestamp']}")

    except ValueError:
        print(f"Erro na conversão da data: {item['timestamp']}")

# função prever_valor_dolar para prever o valor do dólar no próximo dia
ultimo_dia = max(dates)
proximo_dia = ultimo_dia + pd.DateOffset(days=1)
previsao_dolar = prever_valor_dolar(np.array(range(1, len(dates) + 1)).reshape(-1, 1), dollars, len(dates) + 1)

# Código Dash para exibir os resultados
app.layout = html.Div([
    html.H1("Previsão do Valor do Dólar"),
    dcc.Graph(id='grafico-dolar'),
    html.P(f"Previsão do Valor do Dólar para {proximo_dia.date()}: R${previsao_dolar:.2f}")
])

@app.callback(
    Output('grafico-dolar', 'figure'),
    Input('grafico-dolar', 'relayoutData')
)
def update_graph(relayoutData):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=dollars, mode='lines', name='Valor do Dólar'))
    fig.update_layout(title='Histórico do Valor do Dólar',
                      xaxis_title='Data',
                      yaxis_title='Valor do Dólar')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
