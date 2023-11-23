import tkinter as tk
from pytube import YouTube
from moviepy.editor import *
import os
import re
import webbrowser
from instaloader import Instaloader

# Function to simplify the filename
def simplify_filename(title):
    simplified_title = re.sub(r'[^\w\s]', '', title)[:30]
    simplified_title = simplified_title.replace(" ", "_")
    simplified_title = simplified_title.lower()
    return simplified_title

# Function to format time in mm:ss
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

# Function to update progress bar labels
def update_progressbar_labels():
    global video_path
    if video_path:
        video = VideoFileClip(video_path)
        inicio_label.config(text=f"Selecione o tempo de início (mm:ss): 0:00 - {format_time(int(video.duration))}")
        fim_label.config(text=f"Selecione o tempo de fim (mm:ss): 0:00 - {format_time(int(video.duration))}")

# Function to download a video from YouTube
def download_video():
    global video_path, video_loaded
    link = link_entry.get()
    saved_folder = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(saved_folder):
        os.makedirs(saved_folder)
    if 'youtube.com' in link:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_filename = f"{simplify_filename(stream.title)}.mp4"
        video_path = os.path.join(saved_folder, video_filename)
        stream.download(saved_folder, filename=video_filename)
        file_label.config(text=f"Download concluído: {video_filename}")
        update_progressbar_labels()
        carregar_video_salvo()
    elif 'instagram.com' in link:
        loader = Instaloader()
        post = loader.post(link)
        loader.download_post(post, target=saved_folder)
        file_label.config(text=f"Download do vídeo do Instagram concluído.")
        carregar_video_salvo()
    else:
        file_label.config(text="Link não suportado.")

# Function to load saved videos
def carregar_video_salvo():
    global video_path, video_loaded
    saved_folder = os.path.join(os.getcwd(), 'downloads')
    video_files = [os.path.join(saved_folder, f) for f in os.listdir(saved_folder) if f.endswith('.mp4')]
    if video_files:
        video_files.sort(key=os.path.getctime, reverse=True)
        video_path = video_files
    file_label.config(text=f"Vídeo carregado: {os.path.basename(video_path)}")
    if os.path.exists(video_path):
        video = VideoFileClip(video_path)
        update_progressbar_labels()
        video_loaded = True
    else:
        file_label.config(text="O arquivo do vídeo não foi encontrado.")
        video_loaded = False
        file_label.config(text="Nenhum vídeo salvo encontrado.")
        video_loaded = False

# Function to edit the video
def editar_video():
    global video_path
    inicio = inicio_entry.get()
    fim = fim_entry.get()
    extensoes = []
    if mp4_var.get():
        extensoes.append("MP4")
    if mp3_var.get():
        extensoes.append("MP3")
    if video_loaded:
        inicio = sum(x * int(t) for x, t in zip([60, 1], inicio.split(':')))
        fim = sum(x * int(t) for x, t in zip([60, 1], fim.split(':')))
        video = VideoFileClip(video_path)
        edited_video = video.subclip(inicio, fim)
        edited_filename = f"{os.path.splitext(video_path)}-{inicio}-{fim}"
        for extensao in extensoes:
            edited_filename_full = f"{edited_filename}.{extensao.lower()}"
            if extensao == "MP3":
                edited_video.audio.write_audiofile(edited_filename_full)
            else:
                edited_video.write_videofile(edited_filename_full)
        file_label.config(text=f"Vídeo editado salvo como {edited_filename_full}. Editado com sucesso!")
        edited_video.close()
    else:
        file_label.config(text="Você precisa baixar e carregar um vídeo antes de editá-lo")

# Function to open the download folder
def abrir_pasta():
    saved_folder = os.path.join(os.getcwd(), 'downloads')
    if os.path.exists(saved_folder):
        os.startfile(saved_folder)
    else:
        file_label.config(text="Nenhum vídeo foi baixado ainda.")

# Function to open the GitHub repository
def open_github(event):
    webbrowser.open("https://github.com/Rapha29")

# GUI setup
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

link_entry = tk.Entry(frame, bg='light gray', fg=label_color)
link_entry.pack(padx=10, pady=5, fill='x')

file_label = tk.Label(frame, text="", bg='light gray', fg=label_color)
file_label.pack(padx=10, pady=5, anchor='w')

download_button = tk.Button(frame, text="Baixar Vídeo", command=download_video, bg=button_color, fg=button_fg)
download_button.pack(padx=10, pady=5, fill='x')

inicio_label = tk.Label(frame, text="Selecione o tempo de início (mm:ss):", bg='light gray', fg=label_color)
inicio_label.pack(padx=10, pady=5, anchor='w')

inicio_entry = tk.Entry(frame, bg='light gray', fg=label_color)
inicio_entry.pack(padx=10, pady=5, fill='x')

fim_label = tk.Label(frame, text="Selecione o tempo de fim (mm:ss):", bg='light gray', fg=label_color)
fim_label.pack(padx=10, pady=5, anchor='w')

fim_entry = tk.Entry(frame, bg='light gray', fg=label_color)
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

