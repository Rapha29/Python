from flask import Flask, render_template, request
import fitz
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_pdf():
    if request.method == 'POST':
        # Obter o arquivo PDF enviado no formulário
        pdf_file = request.files['pdf_file']
        pdf_data = pdf_file.read()

        # Palavra ou frase a ser procurada
        busca = request.form['busca']

        # Criar um objeto Document do PyMuPDF com o arquivo PDF
        doc = fitz.open(stream=pdf_data, filetype="pdf")

        # Lista para armazenar os resultados da pesquisa
        results = []

        # Pesquisar por palavras-chave em todas as páginas do PDF
        for page_num, page in enumerate(doc.pages()):
            text = page.get_text()
            if busca in text:
                # Obter um trecho do conteúdo onde a palavra-chave foi encontrada
                start_index = text.index(busca)
                end_index = start_index + len(busca)
                excerpt = text[max(0, start_index-50):end_index+50]

                # Adicionar o resultado da pesquisa à lista de resultados
                result = {
                    'pagina': page_num+1,
                    'conteudo': excerpt
                }
                results.append(result)

        # Fechar o arquivo PDF
        doc.close()

        return render_template('results.html', results=results)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
