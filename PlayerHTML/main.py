from flask import Flask, render_template, request

app = Flask(__name__)

def get_video_files():
    video_files = []
    for file in os.listdir('static/videos'):
        if file.endswith('.mp4'):
            video_files.append(file)
    return video_files

@app.route('/')
def index():
    video_files = get_video_files()
    selected_file = request.args.get('file', '')
    return render_template('index.html', videos=video_files, selected_video=selected_file)

if __name__ == '__main__':
    app.run()
