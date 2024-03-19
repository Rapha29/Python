import pandas as pd
from googlesearch import search
import time

# Termo de pesquisa no Google
query = 'site:pagar.me lojas que aceitam pagar.me'

# Lista para armazenar os links das lojas encontradas
links = []

# Realiza a pesquisa no Google e armazena os resultados
for url in search(query, num_results=10):
    print (url)
    links.append(url)
    time.sleep(15)

# Cria um DataFrame do pandas com os links encontrados
df = pd.DataFrame({'Links': links})

# Salva o DataFrame em um arquivo Excel
df.to_excel('lojas_pagar_me.xlsx', index=False)

