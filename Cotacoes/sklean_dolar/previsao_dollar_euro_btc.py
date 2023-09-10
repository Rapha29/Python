from dash import Dash, html, dcc, Input, Output
import requests
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression

app = Dash(__name__)

def prever_valor_moeda(dias_anteriores, valores_da_moeda, proximo_dia):
    modelo = LinearRegression()
    modelo.fit(dias_anteriores, valores_da_moeda)
    previsao = modelo.predict(np.array([proximo_dia]).reshape(-1, 1))
    return previsao[0]

def buscar_dados_moeda(moeda, prazo):
    url = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/{prazo}'
    response = requests.get(url)
    data = response.json()

    dates = []
    values = []

    for item in data:
        try:
            date = pd.to_datetime(int(item['timestamp']), unit='s')
            value = float(item['bid'])

            if not pd.isnull(date):
                dates.append(date)
                values.append(value)
            else:
                print(f"Data inválida: {item['timestamp']}")

        except ValueError:
            print(f"Erro na conversão da data: {item['timestamp']}")

    return dates, values

def buscar_valor_atual(selected_moeda):
    url = f'https://economia.awesomeapi.com.br/json/daily/{selected_moeda}-BRL/1'
    response = requests.get(url)
    data = response.json()
    valor_atual = float(data[0]['bid'])
    return valor_atual

moedas_disponiveis = ['USD', 'EUR', 'BTC']
prazos_disponiveis = [7, 15, 30, 60, 90, 180, 360]

app.layout = html.Div([
    html.H1("Previsão do Valor da Moeda"),
    html.Label("Escolha a moeda:"),
    dcc.RadioItems(
        id='moeda-radio',
        options=[{'label': moeda, 'value': moeda} for moeda in moedas_disponiveis],
        value='USD',  # Moeda padrão
        labelStyle={'display': 'inline-block', 'margin-right': '10px'},
        style={'display': 'flex', 'flexWrap': 'wrap'}  # Alinha os botões de moeda em linha
    ),
    html.Label("Escolha o prazo (dias):"),
    dcc.RadioItems(
        id='prazo-radio',
        options=[{'label': str(prazo), 'value': prazo} for prazo in prazos_disponiveis],
        value=7,  # Prazo padrão
        labelStyle={'display': 'inline-block', 'margin-right': '10px'},
        style={'display': 'flex', 'flexWrap': 'wrap'}  # Alinha os botões de prazo em linha
    ),
    dcc.Graph(id='grafico-moeda'),
    html.Div(id='valor-atual'),
    html.Div(id='previsao-moeda')
])
app.title = "Rapha®"

@app.callback(
    [Output('grafico-moeda', 'figure'), Output('valor-atual', 'children'), Output('previsao-moeda', 'children')],
    [Input('moeda-radio', 'value'), Input('prazo-radio', 'value')]
)
def update_graph(selected_moeda, selected_prazo):
    dates, values = buscar_dados_moeda(selected_moeda, selected_prazo)

    ultimo_dia = max(dates)
    proximo_dia = ultimo_dia + pd.DateOffset(days=1)
    previsao_moeda = prever_valor_moeda(np.array(range(1, len(dates) + 1)).reshape(-1, 1), values, len(dates) + 1)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=values, mode='lines', name=f'Valor da {selected_moeda}'))
    fig.update_layout(title=f'Histórico do Valor da {selected_moeda}',
                      xaxis_title='Data',
                      yaxis_title=f'Valor da {selected_moeda}')

    valor_atual = buscar_valor_atual(selected_moeda)
    previsao_text = f"Previsão do Valor da {selected_moeda} para {proximo_dia.date()}: R${previsao_moeda:.2f}"
    estilo_texto = {'fontSize': '18px', 'marginTop': '10px'}  # Estilo padrão

    if previsao_moeda < valor_atual:
        previsao_text = f"{previsao_text} (Previsão de queda)"
        estilo_texto['color'] = 'red'
    elif previsao_moeda > valor_atual:
        previsao_text = f"{previsao_text} (Previsão de alta)"
        estilo_texto['color'] = 'green'

    return fig, f"Valor atual da {selected_moeda}: R${valor_atual:.2f}", html.Div(previsao_text, style=estilo_texto)

if __name__ == '__main__':
    app.run_server(debug=True)
