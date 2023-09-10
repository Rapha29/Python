from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


def search_in_files(keyword, file_content):
    resultados = []
    try:
        df = pd.read_excel(file_content, sheet_name=None)
    except UnicodeDecodeError:
        # Se a leitura direta do Excel falhar, tente decodificar o arquivo como CSV
        df = pd.read_csv(file_content, sep=None, engine='python', sheet_name=None)

    for sheet_name, df_sheet in df.items():
        mask = df_sheet.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)
        rows = df_sheet[mask]
        if not rows.empty:
            resultado = {
                'Sheet Name': sheet_name,
                'Rows': rows.to_dict('records')  # Convertendo as linhas para uma lista de dicionários
            }
            resultados.append(resultado)
    return resultados


@app.route('/', methods=['GET', 'POST'])
def search_keyword():
    if request.method == 'POST':
        arquivo = request.files['file']
        file_content = arquivo.read()
        keyword = request.form['keyword']
        resultados = search_in_files(keyword, file_content)
        return render_template('resultado.html', resultados=resultados)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

