import openpyxl
import pandas as pd

# Carrega os dados da tabela SKU do primeiro arquivo Excel
arquivo_sku = "SKu.xlsx"
df_sku = pd.read_excel(arquivo_sku)

# Carrega os dados da tabela CNPJs do segundo arquivo Excel
arquivo_cnpjs = "cnpj.xls"
df_cnpjs = pd.read_excel(arquivo_cnpjs)

# Cria a terceira tabela combinando os dados
df_combinado = pd.DataFrame(columns=["SKU", "CNPJ"])

for cnpj in df_cnpjs["CNPJ"]:
    df_combinado = df_combinado.append(pd.DataFrame({"SKU": df_sku["SKU"], "CNPJ": cnpj}))

# Salva a terceira tabela no arquivo Excel
arquivo_combinado = "arquivo_combinado.xlsx"
df_combinado.to_excel(arquivo_combinado, index=False)