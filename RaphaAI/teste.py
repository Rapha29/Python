import os
import fitz

diretorio = r'D:\RaphaAI'
busca = input("Digite a palavra ou frase a ser encontrada: ")
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.pdf'):
        file_path = os.path.join(diretorio, arquivo)
        doc = fitz.open(file_path)
        for page_num, page in enumerate(doc.pages()):
            text = page.get_text()
            if busca in text:
                start_index = text.index(busca)
                end_index = start_index + len(busca)
                excerpt = text[max(0, start_index-50):end_index+50]
                print(f'Arquivo: {arquivo}, Página: {page_num+1}, Conteúdo: {excerpt}')
                print("#"*60)
        doc.close()