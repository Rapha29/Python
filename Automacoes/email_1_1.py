import win32com.client as win32
import openpyxl
import os
import time
from datetime import datetime

# Caminho para o arquivo Excel com a lista de endereços de e-mail
excel_file_path = 'emails.xlsx'

# Caminho para o modelo de e-mail do Outlook (.oft) na mesma pasta do executável
email_template_filename = 'modelo.oft'
email_template_path = os.path.join(os.path.dirname(__file__), email_template_filename)

# Crie uma instância do Outlook
outlook = win32.Dispatch('Outlook.Application')

# Abra o modelo de e-mail
mail = outlook.Session.OpenSharedItem(email_template_path)

# Carregue a lista de e-mails a partir da coluna A da planilha Excel
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# Inicialize a contagem de e-mails enviados
emails_enviados_count = 0

# Limitar o número máximo de e-mails a enviar
max_emails = 499

# Itere pelas linhas da coluna A (que contém os endereços de e-mail)
for cell in sheet['A'][1:]:
    recipient_email = cell.value
    marcacao_enviado = cell.offset(column=4).value

    # Verifique se a coluna 5 (coluna "E") não contém "E-mail Enviado"
    if marcacao_enviado != "E-mail Enviado":
        # Configure o endereço de e-mail do destinatário
        mail.Recipients.Add(recipient_email)

        # Imprima informações no console
        hora_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'E-mail {emails_enviados_count + 1} enviado às {hora_envio} para {recipient_email}')

        # Envie o e-mail
        mail.Send()

        # Atualize a coluna 5 com "E-mail Enviado" na mesma linha
        cell.offset(column=4).value = "E-mail Enviado"

        # Atualize a contagem de e-mails enviados
        emails_enviados_count += 1

        # Salve a planilha após o envio de cada e-mail
        wb.save(excel_file_path)

        # Aguarde 40 segundos antes de enviar o próximo e-mail
        time.sleep(40)

        # Verifique se atingimos o limite máximo de e-mails enviados
        if emails_enviados_count >= max_emails:
            break

print(f'{emails_enviados_count} e-mails enviados com sucesso!')
