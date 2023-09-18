from flask import Flask, request, render_template_string, Markup
from pytube import YouTube
from pathlib import Path
import os
import re

app = Flask(__name__)

# Rota para a página inicial
@app.route("/", methods=["GET"])
def index():
    return render_template_string(get_html_template())

# Rota para o download
@app.route("/download", methods=["GET", "POST"])
def downloadVideo():
    message = ''
    errorType = 0

    if request.method == 'POST' and 'video_url' in request.form:
        youtubeUrl = request.form["video_url"]
        if youtubeUrl:
            validateVideoUrl = (
                r'(https?://)?(www\.)?'
                '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
            validVideoUrl = re.match(validateVideoUrl, youtubeUrl)
            if validVideoUrl:
                url = YouTube(youtubeUrl)
                selected_format = request.form.get("format_option")
                
                if selected_format == "mp4":
                    video = url.streams.get_highest_resolution()
                    ext = "mp4"
                elif selected_format == "mp3":
                    audio_stream = url.streams.filter(only_audio=True).first()
                    ext = "mp3"
                    
                download_folder = str(os.path.join(Path.home(), "Downloads/"))
                os.makedirs(download_folder, exist_ok=True)
                video.download(output_path=download_folder, filename="video." + ext)
                message = 'Video Downloaded Successfully!'
                errorType = 1
            else:
                message = 'Enter Valid YouTube Video URL!'
                errorType = 0
        else:
            message = 'Enter YouTube Video Url.'
            errorType = 0

    return render_template_string(get_html_template(message))

def get_html_template(message=''):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Downloader - MP4</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <img src="/logo.png" alt="Logo" class="logo" width="200">
    <div class="container mt-3">
        <h2>YouTube Downloader</h2>
        <form action="/download" method="post">
            <div class="mb-3 mt-3">
                <label for="video_url">Coloque aqui endereço do YouTube Video:</label>
                <input type="text" class="form-control" id="video_url" placeholder="https://www.youtube.com/watch?v=" name="video_url">
            </div>
            <div class="mb-3">
                <label for="format_option">Escolha o formato:</label>
                <select class="form-select" id="format_option" name="format_option">
                    <option value="mp4">MP4</option>
                    <option value="mp3">MP3</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Download</button>
        </form>
    </div>
    <br><br>
</body>
</html>

    """

if __name__ == "__main__":
    app.run(debug=True)
