from dash import Dash, html, dcc, Input, Output
import requests
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

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
            print(f"Data: {date}, Valor do Dólar: {dollar_value}")
        else:
            print(f"Data inválida: {item['timestamp']}")

    except ValueError:
        print(f"Erro na conversão da data: {item['timestamp']}")

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=dollars, mode='lines', name='Valor do Dólar'))

fig.update_layout(
    title='Cotação do Dólar',
    xaxis_title='Data',
    yaxis_title='Valor do Dólar'
)

app.layout = html.Div(children=[
    html.H1(children='Variação da Cotação do Dólar'),
    dcc.Graph(
        id='grafico_dolar',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
