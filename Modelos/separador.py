import os
import shutil

pasta_origem = r'C:\Users\Admin\Documents\MLWapp2.5'

for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao[1:]
        pasta_destino = os.path.join(pasta_origem, extensao)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
