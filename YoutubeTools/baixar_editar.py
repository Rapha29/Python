#pip install tkinter pytube moviepy 

import tkinter as tk
from pytube import YouTube
from moviepy.editor import *
import os
import re
import webbrowser

# Função para simplificar o nome do arquivo
def simplify_filename(title):
    simplified_title = re.sub(r'[^\w\s]', '', title)[:30]
    simplified_title = simplified_title.replace(" ", "_")  # Substituindo espaços por "_"
    simplified_title = simplified_title.lower()
    return simplified_title

video_path = None
video_loaded = False

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def update_progressbar_labels():
    global video_path
    if video_path:
        video = VideoFileClip(video_path)
        inicio_label.config(text=f"Selecione o tempo de início (mm:ss): 0:00 - {format_time(int(video.duration))}")
        fim_label.config(text=f"Selecione o tempo de fim (mm:ss): 0:00 - {format_time(int(video.duration))}")

def download_video():
    global video_path, video_loaded
    link = link_entry.get()
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    
    saved_folder = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(saved_folder):
        os.makedirs(saved_folder)
    
    video_filename = f"{simplify_filename(stream.title)}.mp4"
    video_path = os.path.join(saved_folder, video_filename)
    stream.download(saved_folder, filename=video_filename)
    
    file_label.config(text=f"Carregamento concluído: {video_filename}")
    update_progressbar_labels()
    carregar_video_salvo()  

def carregar_video_salvo():
    global video_path, video_loaded
    saved_folder = os.path.join(os.getcwd(), 'downloads')  # Caminho para a pasta de downloads
    video_files = [os.path.join(saved_folder, f) for f in os.listdir(saved_folder) if f.endswith('.mp4')]  # Lista todos os arquivos .mp4 na pasta de downloads
    if video_files:  # Verifica se existem arquivos de vídeo na lista
        video_files.sort(key=os.path.getctime, reverse=True)  # Ordena os arquivos pela data de criação, do mais recente ao mais antigo
        video_path = video_files[0]  # Obtém o caminho do vídeo mais recente
        file_label.config(text=f"Vídeo carregado: {os.path.basename(video_path)}")  # Atualiza o rótulo para mostrar o nome do vídeo carregado
        if os.path.exists(video_path):  # Verifica se o arquivo de vídeo existe
            video = VideoFileClip(video_path)  # Carrega o vídeo
            update_progressbar_labels()  # Atualiza as informações da barra de progresso (tempo)
            video_loaded = True  # Indica que o vídeo foi carregado com sucesso
        else:
            file_label.config(text="O arquivo do vídeo não foi encontrado.")  # Informa que o arquivo de vídeo não foi encontrado
            video_loaded = False  # Indica que o vídeo não foi carregado devido à ausência do arquivo
    else:
        file_label.config(text="Nenhum vídeo salvo encontrado.")  # Informa que não há vídeos na pasta de downloads
        video_loaded = False  # Indica que não há vídeo carregado, pois não foram encontrados arquivos na pasta


def editar_video():
    global video_path
    inicio = inicio_entry.get()  # Obtém o tempo de início fornecido pelo usuário
    fim = fim_entry.get()  # Obtém o tempo de fim fornecido pelo usuário
    extensoes = []
    if mp4_var.get():  # Verifica se a opção MP4 está marcada
        extensoes.append("MP4")
    if mp3_var.get():  # Verifica se a opção MP3 está marcada
        extensoes.append("MP3")

    if video_loaded:  # Verifica se um vídeo foi carregado corretamente
        inicio = sum(x * int(t) for x, t in zip([60, 1], inicio.split(':')))  # Converte o tempo de início para segundos
        fim = sum(x * int(t) for x, t in zip([60, 1], fim.split(':')))  # Converte o tempo de fim para segundos

        video = VideoFileClip(video_path)  # Carrega o vídeo original
        edited_video = video.subclip(inicio, fim)  # Corta o vídeo nos intervalos fornecidos pelo usuário

        # Monta o nome do arquivo editado com base no nome original e nos intervalos
        edited_filename = f"{os.path.splitext(video_path)[0]}-{inicio}-{fim}"
        
        for extensao in extensoes:  # Para cada extensão selecionada pelo usuário
            edited_filename_full = f"{edited_filename}.{extensao.lower()}"
            if extensao == "MP3":  # Se a extensão for MP3, salva apenas o áudio
                edited_video.audio.write_audiofile(edited_filename_full)
            else:  # Caso contrário, salva o vídeo com a extensão correspondente
                edited_video.write_videofile(edited_filename_full)
            file_label.config(text=f"Vídeo editado salvo como {edited_filename_full}. Editado com sucesso!")  # Atualiza o rótulo para indicar o sucesso na edição

        edited_video.close()  # Fecha o vídeo editado
    else:
        file_label.config(text="Você precisa baixar e carregar um vídeo antes de editá-lo")  # Indica que o vídeo precisa ser carregado antes da edição


def abrir_pasta():
    saved_folder = os.path.join(os.getcwd(), 'downloads')
    if os.path.exists(saved_folder):
        os.startfile(saved_folder)
    else:
        file_label.config(text="Nenhum vídeo foi baixado ainda.")

def open_github(event):
    webbrowser.open("https://github.com/Rapha29")
    
root = tk.Tk()
root.title("Sem Título")
root.geometry('450x450')
root.configure(bg='light gray')

label_color = 'gray20'
button_color = 'dodger blue'
button_fg = 'white'

frame = tk.Frame(root, bg='light gray')
frame.pack(expand=True, fill='both')

link_label = tk.Label(frame, text="Insira o link do vídeo do YouTube:", bg='light gray', fg=label_color)
link_label.pack(padx=10, pady=5, anchor='w')

link_entry = tk.Entry(frame, bg='white', fg=label_color)
link_entry.pack(padx=10, pady=5, fill='x')

file_label = tk.Label(frame, text="", bg='light gray', fg=label_color)
file_label.pack(padx=10, pady=5, anchor='w')

download_button = tk.Button(frame, text="Carregar Vídeo", command=download_video, bg=button_color, fg=button_fg)
download_button.pack(padx=10, pady=5, fill='x')

inicio_label = tk.Label(frame, text="Selecione o tempo de início (mm:ss):", bg='light gray', fg=label_color)
inicio_label.pack(padx=10, pady=5, anchor='w')

inicio_entry = tk.Entry(frame, bg='white', fg=label_color)
inicio_entry.pack(padx=10, pady=5, fill='x')

fim_label = tk.Label(frame, text="Selecione o tempo de fim (mm:ss):", bg='light gray', fg=label_color)
fim_label.pack(padx=10, pady=5, anchor='w')

fim_entry = tk.Entry(frame, bg='white', fg=label_color)
fim_entry.pack(padx=10, pady=5, fill='x')

extensao_label = tk.Label(frame, text="Selecione o formato de saída:", bg='light gray', fg=label_color)
extensao_label.pack(padx=10, pady=5, anchor='w')

mp4_var = tk.IntVar()
mp3_var = tk.IntVar()

extensao_mp4 = tk.Checkbutton(frame, text="MP4", variable=mp4_var, onvalue=1, offvalue=0, bg='light gray', fg='black')
extensao_mp4.pack(padx=10, pady=5, anchor='w')

extensao_mp3 = tk.Checkbutton(frame, text="MP3", variable=mp3_var, onvalue=1, offvalue=0, bg='light gray', fg='black')
extensao_mp3.pack(padx=10, pady=5, anchor='w')

editar_button = tk.Button(frame, text="Editar Vídeo", command=editar_video, bg=button_color, fg=button_fg)
editar_button.pack(padx=10, pady=5, fill='x')

abrir_pasta_button = tk.Button(frame, text="Abrir Pasta", command=abrir_pasta, bg=button_color, fg=button_fg)
abrir_pasta_button.pack(padx=10, pady=5, fill='x')

# Footer
footer_frame = tk.Frame(root, bg='light gray')
footer_frame.pack(side='bottom', fill='x')

reserved_label = tk.Label(footer_frame, text="Todos os direitos reservados: ", bg='light gray', fg='black')
reserved_label.pack(side='left')

rapha_link = tk.Label(footer_frame, text="Rapha®", bg='light gray', fg='blue', cursor='hand2')
rapha_link.pack(side='left')
rapha_link.bind("<Button-1>", open_github)

root.mainloop()

''' FAZER DEPLOY EXECUTAVEL
pip install pyinstaller
pyinstaller --onefile --hidden-import=tkinter --hidden-import=pytube --hidden-import=moviepy --hidden-import=os --hidden-import=re --hidden-import=webbrowser --noconsole d:/Repositorio/Python/YoutubeTools/baixar_editar.py
'''

