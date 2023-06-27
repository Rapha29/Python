import os
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from pytube import exceptions as pytube_exceptions
from moviepy.editor import AudioFileClip


def baixar_video():
    url = url_entry.get()
    formato = formato_combo.get()

    try:
        yt = YouTube(url)

        if formato == 'mp3':
            try:
                stream = yt.streams.filter(only_audio=True).first()
            except pytube_exceptions.RegexMatchError:
                progress_var.set("Não foi possível encontrar uma versão somente de áudio.")
                root.update()
                return

            progress_var.set("Baixando...")
            root.update()
            file_path = stream.download(output_path="videos")
            progress_var.set("Download concluído. Convertendo para mp3...")
            root.update()

            clip = AudioFileClip(file_path)
            clip.write_audiofile(file_path.replace(".mp4", ".mp3"))

            os.remove(file_path)
            progress_var.set("Conversão concluída.")
            root.update()
        else:
            if formato == 'mkv':
                stream = yt.streams.filter(file_extension='webm').get_highest_resolution()
            elif formato == 'mp4':
                stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

            progress_var.set("Baixando...")
            root.update()
            stream.download(output_path="videos")
            progress_var.set("Download concluído.")
            root.update()

    except pytube_exceptions.VideoUnavailable:
        progress_var.set("O vídeo solicitado não está disponível.")
        root.update()
    except Exception as e:
        progress_var.set("Ocorreu um erro durante o processo: {}".format(str(e)))
        root.update()


root = tk.Tk()
root.geometry('600x400')
root.title("DownTube - Baixador de Vídeos do YouTube")

logo = tk.PhotoImage(file="logo.png")
logo_label = ttk.Label(root, image=logo)
logo_label.pack(pady=10)

dev_label = ttk.Label(root, text="Desenvolvido por:")
dev_label.pack()
dev_label.pack(pady=10)

title = ttk.Label(root, text="DownTube - Baixador de Vídeos do YouTube", font=("Helvetica", 16))
title.pack(pady=10)

url_label = ttk.Label(root, text="URL do YouTube:")
url_label.pack()

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

formato_label = ttk.Label(root, text="Formato:")
formato_label.pack()

formato_combo = ttk.Combobox(root, values=["mp3", "mp4", "mkv"], state="readonly")
formato_combo.pack(pady=5)

download_button = ttk.Button(root, text="Baixar", command=baixar_video)
download_button.pack(pady=10)

progress_var = tk.StringVar()
progress_var.set("Esperando...")

progress_label = ttk.Label(root, textvariable=progress_var)
progress_label.pack()

root.mainloop()
