import pandas as pd

df = pd.read_excel('1.xlsx', sheet_name=None)
for sheet_name in df.keys():
    df[sheet_name] = df[sheet_name].astype(str)

palavra_chave = input("Digite sua busca: ")
for sheet_name, sheet_df in df.items():
    resultado = sheet_df.apply(lambda x: x.str.contains(palavra_chave, case=False))
    linhas_com_palavra_chave = sheet_df[resultado.any(axis=1)]
    for indice, linha in linhas_com_palavra_chave.iterrows():
        print(f"A palavra-chave '{palavra_chave}' foi encontrada na planilha '{sheet_name}', linha {indice + 1}:")
        print(linha)
        print()

# fazer ler no navegador
# botao upload
# abrir campo de pesquisa
# retornar todas as entradas encontradas