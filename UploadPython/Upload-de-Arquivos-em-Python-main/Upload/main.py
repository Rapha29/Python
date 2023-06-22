import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    file = request.files['file']
    file.save(os.path.join('arquivos', file.filename))
    return f'Arquivo "{file.filename}" carregado com sucesso! <a href="/">Voltar</a>'
  else:
    return '''
          <h1>Upload de arquvios</h1>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit">
            </form>
            <hr>
            <h2>Lista de Arquivos</h2>
            {}
            {}
            <style>
               img {{
                    margin: 10px;
                }}
            </style>
        '''.format(get_file_list(), get_image_gallery())


@app.route('/arquivos/<filename>')
def download(filename):
  return send_from_directory('./arquivos', filename)


def get_file_list():
  files = [
    f for f in os.listdir('./arquivos')
    if os.path.isfile(os.path.join('./arquivos', f))
  ]
  file_groups = {}
  for f in files:
    ext = os.path.splitext(f)[1]
    if ext.lower() == '.pdf':
      file_groups.setdefault('PDF', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.txt':
      file_groups.setdefault('TXT', []).append(f'/arquivos/{f}')
    elif ext.lower() in ['.jpg', '.jpeg']:
      file_groups.setdefault('JPG', []).append(f'/arquivos/{f}')
  file_list = ''
  for ext, urls in file_groups.items():
    if ext == 'PDF' or ext == 'TXT':
      file_list += f'<h3>{ext}</h3><ul>'
      for url in urls:
        filename = os.path.basename(url)
        file_list += f'<li><a href="{url}">{filename}</a></li>'
      file_list += '</ul>'
  return file_list


def get_image_gallery():
  files = [
    f for f in os.listdir('./arquivos')
    if os.path.isfile(os.path.join('./arquivos', f))
    and os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg']
  ]
  gallery = ''
  for f in files:
    url = f'/arquivos/{f}'
    gallery += f'<a href="{url}" target="_blank"><img src="{url}" alt="{f}" width="200"></a>'
  if gallery:
    gallery = '<hr><h2>Galeria de Imagens</h2>' + gallery
  return gallery


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
