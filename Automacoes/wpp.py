import pywhatkit as kit
import openpyxl
import pyautogui
import time
import locale
import keyboard
import os

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def enviar_mensagem_whatsapp(numero, mensagem):
    kit.sendwhatmsg_instantly(numero, mensagem) 

# Obtém o caminho completo para o arquivo "dados.xlsx" na mesma pasta que o script
caminho_arquivo_excel = os.path.join(os.path.dirname(__file__), 'dados.xlsx')

wb = openpyxl.load_workbook(caminho_arquivo_excel)
planilha = wb.active

time.sleep(5)

try:
    for row in planilha.iter_rows(min_row=2, values_only=True):
        Nome = row[0]
        Numero = "+55" + str(row[1])
        Enviar = row[2]
                
        if Enviar == None:
            pyautogui.hotkey("ctrl", "w")
            print(f"Pulando {Nome}")
        else:
            pyautogui.press("esc")
            mensagem_personalizada = f'Olá {Nome}, só passando para avisar que em breve teremos mais conteúdos'
            enviar_mensagem_whatsapp(Numero, mensagem_personalizada)
            time.sleep(1)
            pyautogui.press("Enter")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(1)
            print(f"Mensagem Enviada com sucesso para: {Nome}")
        
        if keyboard.is_pressed('q'):
            print("Encerramento manual detectado, parando scripts...")
            break
except Exception as e:
    
    
    print(f'Algo estranho aconteceu: {e}')
finally:
    wb.close()
