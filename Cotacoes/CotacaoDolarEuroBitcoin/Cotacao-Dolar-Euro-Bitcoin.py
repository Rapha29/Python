from dash import Dash, html, dcc, Input, Output
import requests
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/15'
response = requests.get(url)
data = response.json()

dates = []
bids = []
asks = []

for item in data:
    dates.append(pd.to_datetime(item['timestamp'], dayfirst=True))
    bids.append(float(item['bid']))
    asks.append(float(item['ask']))

df = pd.DataFrame({'date': dates, 'bid': bids, 'ask': asks})

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['date'], y=df['bid'], mode='lines', name='Bid'))

app.layout = html.Div(children=[
    html.H1(children='Variação do Dólar'),
    dcc.Graph(
        id='grafico_dolar',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)