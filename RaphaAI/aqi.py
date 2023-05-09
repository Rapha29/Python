import os
import fitz
# instalar a biblioteca PyMuPDF

# Diretório onde os arquivos PDF estão armazenados
diretorio = r'D:\RaphaAI'

# Palavra ou frase a ser procurada
busca = input("Digite a palavra ou frase a ser encontrada: ")

# Loop através de todos os arquivos na pasta
for arquivo in os.listdir(diretorio):
    # Verificar se o arquivo é um arquivo PDF
    if arquivo.endswith('.pdf'):
        # Abrir o arquivo PDF usando o PyMuPDF
        file_path = os.path.join(diretorio, arquivo)
        doc = fitz.open(file_path)

        # Pesquisar por palavras-chave em todas as páginas do PDF
        for page_num, page in enumerate(doc.pages()):
            text = page.get_text()
            if busca in text:
                # Obter um trecho do conteúdo onde a palavra-chave foi encontrada
                start_index = text.index(busca)
                end_index = start_index + len(busca)
                excerpt = text[max(0, start_index-50):end_index+50]

                # Imprimir o número da página e o trecho do conteúdo onde a palavra-chave foi encontrada
                print(f'Arquivo: {arquivo}, Página: {page_num+1}, Conteúdo: {excerpt}')
                print("#"*60)

        # Fechar o arquivo PDF
        doc.close()