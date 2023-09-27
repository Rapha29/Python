import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import win32com.client as win32
import openpyxl
import os
import threading
from datetime import datetime
import time
import schedule

# Variáveis globais para controle do envio de e-mails
enviando_emails = False
max_emails = 499 # Limite do Gmail por dia
emails_enviados_count = 0
email_template = ""  # Variável para armazenar o modelo de e-mail
email_subject = ""   # Variável para armazenar o assunto do e-mail
intervalo_envio = 15  # Intervalo padrão entre o envio de e-mails (em segundos)

# Variáveis para a contagem regressiva
contador_intervalo_var = None
contador_intervalo_segundos = 0

# Função para enviar e-mails em uma thread separada
def enviar_emails_thread():
    global enviando_emails, max_emails, emails_enviados_count, email_template, email_subject, intervalo_envio, contador_intervalo_segundos
    
    excel_file_path = entrada_arquivo_excel.get()
    
    outlook = win32.Dispatch('Outlook.Application')
    
    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb.active
    
    for cell in sheet['A'][1:]:
        if not enviando_emails:
            break
            
        recipient_email = cell.value
        marcacao_enviado = cell.offset(column=4).value

        if marcacao_enviado != "E-mail Enviado":
            try:
                mail = outlook.CreateItem(0)  # Cria um novo email
                mail.Subject = email_subject  # Use o assunto do e-mail definido pelo usuário
                
                hora_envio = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                status_msg = f'E-mail enviado para {recipient_email} às {hora_envio}'
                lista_emails.insert(0, status_msg)
                print(status_msg)  # Mostra a mensagem de status no terminal

                mail.To = recipient_email
                mail.Body = email_template  # Use o modelo de e-mail definido pelo usuário
                mail.Send()
                cell.offset(column=4).value = "E-mail Enviado"
                cell.offset(column=5).value = hora_envio
                
                emails_enviados_count += 1
                wb.save(excel_file_path)
                
                if emails_enviados_count >= max_emails:
                    enviando_emails = False
                    break
                
                # Aguarda o intervalo definido pelo usuário antes de enviar o próximo e-mail
                for segundos in range(intervalo_envio, 0, -1):
                    if not enviando_emails:
                        break
                    contador_intervalo_var.set(f'Intervalo: {segundos} segundos')
                    time.sleep(1)
                    contador_intervalo_segundos = segundos
            except Exception as e:
                # Lidar com exceções de envio de e-mail
                error_msg = f"Erro ao enviar e-mail para {recipient_email}: {str(e)}"
                print(error_msg)

    if not enviando_emails:
        messagebox.showinfo("Parado", f'Envio de e-mails interrompido. Total de {emails_enviados_count} e-mails enviados.')
        print(f'Envio de e-mails interrompido. Total de {emails_enviados_count} e-mails enviados.')
    else:
        messagebox.showinfo("Concluído", f'{emails_enviados_count} e-mails enviados com sucesso.')
        print(f'{emails_enviados_count} e-mails enviados com sucesso.')
    
    enviando_emails = False
    contador_intervalo_var.set('Intervalo: 0 segundos')

# Função para iniciar o envio de e-mails em uma thread separada
def iniciar_envio():
    global enviando_emails, max_emails, emails_enviados_count, email_template, email_subject, intervalo_envio, contador_intervalo_segundos
    
    if not enviando_emails:
        enviando_emails = True
        max_emails = int(entrada_max_emails.get())
        emails_enviados_count = 0
        email_subject = entrada_assunto_email.get()  # Obtenha o assunto do e-mail
        email_template = entrada_email_template.get("1.0", tk.END)  # Obtenha o conteúdo do campo de entrada de texto
        intervalo_envio = int(entrada_intervalo_envio.get())  # Obtenha o intervalo de envio definido pelo usuário
        lista_emails.delete(0, tk.END)  # Limpe o campo de status
        print("Iniciando envio de e-mails...")  # Mensagem de status no terminal
        
        # Inicie uma nova thread para enviar e-mails
        enviar_thread = threading.Thread(target=enviar_emails_thread)
        enviar_thread.start()
        contador_intervalo_var.set(f'Intervalo: {intervalo_envio} segundos')
        contador_intervalo_segundos = intervalo_envio

def parar_envio():
    global enviando_emails
    enviando_emails = False

def enviar_e_receber_emails_outlook():
    outlook = win32.Dispatch('Outlook.Application')
    outlook.GetNamespace("MAPI").SendAndReceive()
    print("E-mails do Outlook enviados e recebidos.")

def agendar_enviar_e_receber_emails():
    schedule.every(1).minutes.do(enviar_e_receber_emails_outlook)

root = tk.Tk()
root.title("Envio de E-mails (Com Outlook)")

# Função para criar e posicionar widgets com largura total e margem
def criar_widget_frame(parent, text):
    frame = tk.Frame(parent)
    frame.pack(pady=5, fill=tk.X)
    label = tk.Label(frame, text=text, width=20, anchor="w")
    label.pack(side=tk.LEFT, padx=5)
    return frame

frame_arquivo_excel = criar_widget_frame(root, "Arquivo Excel:")
entrada_arquivo_excel = tk.Entry(frame_arquivo_excel)
entrada_arquivo_excel.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

botao_procurar_excel = tk.Button(frame_arquivo_excel, text="Procurar", command=lambda: entrada_arquivo_excel.insert(0, filedialog.askopenfilename()))
botao_procurar_excel.pack(side=tk.LEFT, padx=(0, 5))

frame_assunto_email = criar_widget_frame(root, "Assunto do E-mail:")
entrada_assunto_email = tk.Entry(frame_assunto_email)
entrada_assunto_email.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

frame_email_template = criar_widget_frame(root, "Modelo de E-mail:")
entrada_email_template = tk.Text(frame_email_template, width=40, height=10)
entrada_email_template.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

frame_max_emails = criar_widget_frame(root, "Número Máximo de E-mails:")
entrada_max_emails = tk.Entry(frame_max_emails)
entrada_max_emails.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

frame_intervalo_envio = criar_widget_frame(root, "Intervalo entre Envios\n (segundos):")
entrada_intervalo_envio = tk.Entry(frame_intervalo_envio)
entrada_intervalo_envio.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

frame_botoes = criar_widget_frame(root, "")
botao_iniciar = tk.Button(frame_botoes, text="Iniciar Envio", command=iniciar_envio)
botao_iniciar.pack(side=tk.LEFT)
botao_parar = tk.Button(frame_botoes, text="Parar Envio", command=parar_envio)
botao_parar.pack(side=tk.LEFT)

# Novo display de status
frame_status_novo = tk.Frame(root)
frame_status_novo.pack(pady=5, fill=tk.X)
label_status_novo = tk.Label(frame_status_novo, text="Status:")
label_status_novo.pack(side=tk.LEFT, padx=5)
contador_intervalo_var = tk.StringVar()
contador_intervalo_label = tk.Label(frame_status_novo, textvariable=contador_intervalo_var)
contador_intervalo_label.pack(side=tk.LEFT, padx=5)
contador_intervalo_var.set('Intervalo: 0 segundos')

frame_status = criar_widget_frame(root, "")
lista_emails = tk.Listbox(frame_status, width=100, height=10)
lista_emails.pack(padx=(0, 5))

# Agende o envio e recebimento de e-mails a cada 1 minuto
agendar_enviar_e_receber_emails()

root.mainloop()
