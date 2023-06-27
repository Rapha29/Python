import openpyxl
import pandas as pd

arquivo_sku = "SKU.xlsx"# Carrega os dados da tabela SKU do primeiro arquivo Excel
df_sku = pd.read_excel(arquivo_sku)
arquivo_cnpjs = "cnpj.xlsx"
df_cnpjs = pd.read_excel(arquivo_cnpjs, header=None, names=["CNPJ"])

df_combinado = pd.DataFrame(columns=["SKU", "CNPJ"])# Cria a tabela combinando

for cnpj in df_cnpjs["CNPJ"]:
    df_temp = pd.DataFrame({"SKU": df_sku["Cód. Item"], "CPF/CNPJ": cnpj})
    df_combinado = pd.concat([df_combinado, df_temp], ignore_index=True)

arquivo_combinado = "arquivo_combinado.csv" # Noma da planilha
df_combinado.to_csv(arquivo_combinado, index=False)
