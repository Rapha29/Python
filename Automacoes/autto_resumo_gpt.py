import PyPDF2
from PyPDF2 import PdfFileReader
import openai
import os

# Configurar a chave da API do OpenAI
openai.api_key = "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"

# Prompt inicial com as instruções para o GPT
prompt_inicial = "Vou enviar um livro, página por página, e quero que aguarde a frase 'livro enviado por completo' antes de fazer o resumo. Após essa frase, quero um resumo completo do conteúdo, separado por seus respectivos títulos e de forma fácil de entender."

# Enviar o prompt inicial para o GPT
response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=prompt_inicial,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.7,
)

# Caminho para o arquivo PDF (na mesma pasta do código)
caminho_pdf = "livro.pdf"

# Abrir o arquivo PDF
with open(caminho_pdf, "rb") as arquivo_pdf:
    leitor_pdf = PdfFileReader(arquivo_pdf)
    numero_paginas = leitor_pdf.getNumPages()

    # Criar um objeto de conteúdo
    conteudo_livro = ""

    # Enviar cada página para o GPT
    for pagina in range(numero_paginas):
        pagina_atual = leitor_pdf.getPage(pagina)
        texto_pagina = pagina_atual.extractText()
        conteudo_livro += texto_pagina

        # Enviar o texto da página para o GPT
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=texto_pagina,
            max_tokens=1,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Imprimir a resposta do GPT (opcional)
        print(response.choices[0].text)

    # Após enviar todas as páginas, enviar o prompt "livro enviado por completo"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="livro enviado por completo",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Obter o resumo completo do livro
    resumo_livro = response.choices[0].text

    # Salvar o resumo em um arquivo
    with open("resumo_livro.txt", "w", encoding="utf-8") as arquivo_resumo:
        arquivo_resumo.write(resumo_livro)

    print("Resumo do livro salvo em 'resumo_livro.txt'")